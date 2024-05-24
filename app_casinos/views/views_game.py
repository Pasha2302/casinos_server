from rest_framework.pagination import PageNumberPagination

from app_casinos.models.casino import Game
from app_casinos.serializers import GameSerializer
from app_casinos.views.objects_for_general_import import *


class CustomPagination(PageNumberPagination):
    page_size = 250  # количество объектов на странице
    page_size_query_param = 'page_size'
    max_page_size = 250


class GameListCreateAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = CustomPagination


class GameFilterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data_filter = request.data.get('data_filter', [])
        # Пример запроса к базе данных (замените на свой код)
        queryset = Game.objects.filter(name__in=data_filter)
        # Сериализация данных
        serializer = GameSerializer(queryset, many=True)

        return Response(serializer.data)