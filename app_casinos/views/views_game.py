from app_casinos.serializers import *


class DeleteAllDataGameAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        Game.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class GameListCreateAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer