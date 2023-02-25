from django.contrib.auth import get_user_model
from rest_framework import serializers

from system_for_remote_meter_points.SIM.models import SIM
from system_for_remote_meter_points.meter_devices.models import MeterDevice
from system_for_remote_meter_points.meter_points.models import MeterPoint
from system_for_remote_meter_points.modems.models import Modem
from system_for_remote_meter_points.tasks.models import Task

UserModel = get_user_model()


class ShortModemApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modem
        fields = '__all__'


class ShortMeterDeviceApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterDevice
        fields = '__all__'


class ShortUserApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'department', 'picture',)


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


class MeterDeviceApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterDevice
        fields = '__all__'


class MeterDeviceCreateApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterDevice
        fields = '__all__'

    def create(self, validated_data):
        return MeterDevice.objects.create(**validated_data)


class TaskApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        return Task.objects.create(**validated_data)



class MeterPointApiSerializer(serializers.ModelSerializer):
    modem = ShortModemApiSerializer()
    meter_device = ShortMeterDeviceApiSerializer()
    user = ShortUserApiSerializer()
    class Meta:
        model = MeterPoint
        fields = '__all__'


class MeterPointCreateApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterPoint
        fields = '__all__'

    def create(self, validated_data):
        return MeterPoint.objects.create(**validated_data)

