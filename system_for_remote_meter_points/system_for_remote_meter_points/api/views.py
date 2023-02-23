from django.contrib.auth import get_user_model
from rest_framework import generics as rest_views

from system_for_remote_meter_points.SIM.models import SIM
from system_for_remote_meter_points.api.serializers import UserApiSerializer, UserCreateApiSerializer, SIMApiSerializer, \
    SIMCreateApiSerializer, ModemApiSerializer, ModemCreateApiSerializer
from system_for_remote_meter_points.modems.models import Modem

UserModel = get_user_model()


class UserListApiView(rest_views.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserApiSerializer


class UserCreateApiView(rest_views.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserCreateApiSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class UserUpdateApiView(rest_views.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserApiSerializer
    lookup_field = 'pk'


class UserDeleteApiView(rest_views.RetrieveDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserApiSerializer
    lookup_field = 'pk'


class SIMListApiView(rest_views.ListAPIView):
    queryset = SIM.objects.all()
    serializer_class = SIMApiSerializer


class SIMCreateApiView(rest_views.ListCreateAPIView):
    queryset = SIM.objects.all()
    serializer_class = SIMCreateApiSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class SIMUpdateApiView(rest_views.RetrieveUpdateAPIView):
    queryset = SIM.objects.all()
    serializer_class = SIMApiSerializer
    lookup_field = 'pk'


class SIMDeleteApiView(rest_views.RetrieveDestroyAPIView):
    queryset = SIM.objects.all()
    serializer_class = SIMApiSerializer
    lookup_field = 'pk'


class ModemListApiView(rest_views.ListAPIView):
    queryset = Modem.objects.all()
    serializer_class = ModemApiSerializer


class ModemCreateApiView(rest_views.ListCreateAPIView):
    queryset = Modem.objects.all()
    serializer_class = ModemCreateApiSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class ModemUpdateApiView(rest_views.RetrieveUpdateAPIView):
    queryset = Modem.objects.all()
    serializer_class = ModemApiSerializer
    lookup_field = 'pk'


class ModemDeleteApiView(rest_views.RetrieveDestroyAPIView):
    queryset = Modem.objects.all()
    serializer_class = ModemApiSerializer
    lookup_field = 'pk'

