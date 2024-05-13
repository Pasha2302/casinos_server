from rest_framework import viewsets, status
from rest_framework.response import Response

from app_casinos.models.bonus import DataAutoFillBonus
from app_casinos.serializers import DataAutoFillBonusSerializer


class DataAutoFillBonusViewSet(viewsets.ModelViewSet):
    queryset = DataAutoFillBonus.objects.all()
    serializer_class = DataAutoFillBonusSerializer

    def create(self, request):
        # Создание нового объекта
        # print(f"\n\nМетод <create>\nRequest: {request}\nSelf: {self}")
        name = request.data.get('name')
        if DataAutoFillBonus.objects.filter(name=name).exists():
            return Response({'data': 'Name already exists', 'status': "False"},)

        serializer = DataAutoFillBonusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # Получение объекта по полю 'name'
        queryset = DataAutoFillBonus.objects.filter(name=pk)
        if queryset.exists():
            serializer = DataAutoFillBonusSerializer(queryset.first())
            return Response(serializer.data)
        else:
            # return Response({"data": "False"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"data": False})

    def update(self, request, pk=None):
        # Обновление данных объекта по полю 'name'
        queryset = DataAutoFillBonus.objects.filter(name=pk)
        if queryset.exists():
            serializer = DataAutoFillBonusSerializer(queryset.first(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

