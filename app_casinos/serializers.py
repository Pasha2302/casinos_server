from rest_framework import serializers

from app_casinos.models.bonus import DataAutoFillBonus
from app_casinos.models.casino import (
    Game, Casino,
)


class CasinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casino
        fields = "__all__"


class CasinoFilterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casino
        fields = ['id', 'is_pars_data', 'slug', 'link_casino_guru']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name')


class DataAutoFillBonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAutoFillBonus
        fields = ('name', 'data')

