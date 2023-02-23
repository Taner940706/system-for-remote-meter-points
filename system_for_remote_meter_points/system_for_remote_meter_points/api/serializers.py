from django.contrib.auth import get_user_model
from rest_framework import serializers

from system_for_remote_meter_points.SIM.models import SIM
from system_for_remote_meter_points.modems.models import Modem

UserModel = get_user_model()


class UserApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'department', 'picture',)


class UserCreateApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'department', 'picture',)

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)


class SIMApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SIM
        fields = '__all__'


class SIMCreateApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SIM
        fields = '__all__'

    def create(self, validated_data):
        return SIM.objects.create(**validated_data)


class ModemApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modem
        fields = '__all__'


class ModemCreateApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modem
        fields = '__all__'

    def create(self, validated_data):
        return Modem.objects.create(**validated_data)

