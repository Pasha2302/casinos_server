from app_casinos.serializers import *


class DeleteAllDataProviderAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        Provider.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class ProviderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
