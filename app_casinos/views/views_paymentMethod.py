from app_casinos.serializers import *


class DeleteAllDataPaymentMethodAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        PaymentMethod.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class PaymentMethodListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer