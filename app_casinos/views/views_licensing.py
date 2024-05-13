from app_casinos.views.objects_for_general_import import *

from app_casinos.models.casino import LicensingAuthority
from app_casinos.serializers import LicensingAuthoritySerializer


class DeleteAllDataLicensingAuthorityAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        LicensingAuthority.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class LicensingAuthorityListCreateAPIView(generics.ListCreateAPIView):
    queryset = LicensingAuthority.objects.all()
    serializer_class = LicensingAuthoritySerializer
