from app_casinos.models.casino import PaymentMethod
from app_casinos.serializers import PaymentMethodSerializer
from app_casinos.views.objects_for_general_import import *


class DeleteAllDataPaymentMethodAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        PaymentMethod.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class PaymentMethodListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer