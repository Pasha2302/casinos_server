from app_casinos.models.casino import Language
from app_casinos.serializers import LanguageSerializer
from app_casinos.views.objects_for_general_import import *


class DeleteAllDataLanguageAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        Language.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class LanguageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer