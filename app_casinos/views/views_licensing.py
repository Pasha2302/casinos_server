from app_casinos.serializers import *


class DeleteAllDataLicensingAuthorityAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        LicensingAuthority.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class LicensingAuthorityListCreateAPIView(generics.ListCreateAPIView):
    queryset = LicensingAuthority.objects.all()
    serializer_class = LicensingAuthoritySerializer
