from app_casinos.models.casino import GameType
from app_casinos.serializers import GameTypeSerializer
from app_casinos.views.objects_for_general_import import *


class DeleteAllDataGameTypeAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        GameType.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class GameTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = GameType.objects.all()
    serializer_class = GameTypeSerializer