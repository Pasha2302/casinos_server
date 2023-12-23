from app_casinos.serializers import *


class DeleteAllDataLanguageAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        Language.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class LanguageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer