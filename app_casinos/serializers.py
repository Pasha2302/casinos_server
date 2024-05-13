from rest_framework import serializers

from app_casinos.models.bonus import DataAutoFillBonus
from app_casinos.models.casino import (
    ClassicCurrency, CryptoCurrency, Provider, Country,
    LicensingAuthority, Language,GameType, Game, PaymentMethod
)


class LicensingAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = LicensingAuthority
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameType
        fields = '__all__'


class ClassicCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassicCurrency
        fields = '__all__'

class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = '__all__'



class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class GameSerializerFilter(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name')


class DataAutoFillBonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAutoFillBonus
        fields = ('name', 'data')
