from app_casinos.serializers import CountrySerializer
from app_casinos.views.objects_for_general_import import *

from app_casinos.models.casino import Country


class DeleteAllDataCountryAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        Country.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer