import json # REVIEW: Этот модуль нигде не используется
from django.http import HttpResponse # REVIEW: Этот модуль нигде не используется
from rest_framework import generics # REVIEW: Этот модуль нигде не используется
from rest_framework.response import Response # REVIEW: Этот модуль нигде не используется
from rest_framework.views import APIView # REVIEW: Этот модуль нигде не используется
# REVIEW: Тут непонятно, зачем пустая строка нужна
from rest_framework import serializers
from app_casinos.all_models.models import (
    ClassicCurrency, CryptoCurrency, Provider, Country,
    LicensingAuthority, Language,GameType, Game, PaymentMethod # REVIEW: Тут не хватает пробела между Language и GameType
)


class LicensingAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = LicensingAuthority
        fields = '__all__'
# REVIEW: Между классами должно быть две пустые строки, а не одна
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
# REVIEW: И не три


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
