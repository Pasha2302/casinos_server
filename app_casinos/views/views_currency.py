from django.http import HttpResponse
from rest_framework.utils import json

from app_casinos.models.casino import ClassicCurrency, CryptoCurrency
from app_casinos.serializers import CryptoCurrencySerializer, ClassicCurrencySerializer
from app_casinos.views.objects_for_general_import import *


class DeleteAllDataCurrencyAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        ClassicCurrency.objects.all().delete()
        CryptoCurrency.objects.all().delete()

        return Response({"message": "All data deleted successfully."})


class CryptoCurrencyListCreateAPIView(generics.ListCreateAPIView):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer

class CurrencyListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClassicCurrency.objects.all()
    serializer_class = ClassicCurrencySerializer


class CurrencyDataAPIView(generics.ListAPIView):
    serializer_class = ClassicCurrencySerializer

    def list(self, request, *args, **kwargs):
        classic_currencies = ClassicCurrency.objects.all()
        crypto_currencies = CryptoCurrency.objects.all()

        classic_serializer = ClassicCurrencySerializer(classic_currencies, many=True)
        crypto_serializer = CryptoCurrencySerializer(crypto_currencies, many=True)

        data = {
            'classic_currencies': classic_serializer.data,
            'crypto_currencies': crypto_serializer.data,
        }

        # Преобразуйте данные в JSON-строку
        json_data = json.dumps(data, indent=2)

        # Создайте ответ с JSON-данными
        response = HttpResponse(json_data, content_type='application/json')

        # Задайте заголовок Content-Disposition для указания имени файла
        response['Content-Disposition'] = 'attachment; filename="currency_data.json"'

        return response
