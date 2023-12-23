from app_casinos.serializers import *


class DeleteAllDataCountryAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        Country.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer