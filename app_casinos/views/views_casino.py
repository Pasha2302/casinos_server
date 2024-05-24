from django.middleware.csrf import get_token
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from app_casinos.models.casino import Casino, SisterCasino, Provider, PaymentMethod
from app_casinos.serializers import CasinoSerializer, CasinoFilterDataSerializer
from app_casinos.views.objects_for_general_import import *



class CustomPagination(PageNumberPagination):
    # Можно настроить параметры пагинации
    page_size = 100  # Количество объектов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания размера страницы
    max_page_size = 100  # Максимальное количество объектов на странице


class AddDataCasinoAPIView(APIView):

    @staticmethod
    def add_data(data, _model):
        ids = []
        for name in data:
            # Проверяем, существует ли запись с таким именем
            data_id, created = _model.objects.get_or_create(name=name)
            ids.append(data_id.id)
        return ids

    def post(self, request, format=None):
        created_data_ids = {'sisters_casinos': [], 'providers': [], 'payment_methods': []}
        data_sisters_casinos = request.data.get('sisters_casinos', [])
        data_providers = request.data.get('providers', [])
        data_payment_methods = request.data.get('payment_methods', [])
        datas = [
            (data_sisters_casinos, SisterCasino, 'sisters_casinos'),
            (data_providers, Provider, 'providers'),
            (data_payment_methods, PaymentMethod, 'payment_methods'),
        ]

        for data, model, key in datas:
            data = self.add_data(data, model)
            if data: created_data_ids[key].extend(data)

        return Response({'created_data_ids': created_data_ids}, status=status.HTTP_201_CREATED)


class CasinoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializer
    # обновлять объекты по "slug", а не первичному ключу "pk"
    lookup_field = 'slug'

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'message': {'data updated': True}}, status=status.HTTP_200_OK)


class CasinoFilteredListAPIView(APIView):
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        casinos = Casino.objects.filter(is_pars_data=False)
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(casinos, request)
        if page is not None:
            serializer = CasinoFilterDataSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = CasinoFilterDataSerializer(casinos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CSRFTokenAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Получаем CSRF-токен
        csrf_token = get_token(request)
        return Response({'csrf_token': csrf_token})
