from app_casinos.serializers import *


class DeleteAllDataGameTypeAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        GameType.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class GameTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = GameType.objects.all()
    serializer_class = GameTypeSerializer