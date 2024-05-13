from app_casinos.models.casino import Provider
from app_casinos.serializers import ProviderSerializer
from app_casinos.views.objects_for_general_import import *


class DeleteAllDataProviderAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        Provider.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class ProviderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
