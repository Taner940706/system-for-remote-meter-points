from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import generics as rest_views
from rest_framework.response import Response

from system_for_remote_meter_points.SIM.models import SIM
from system_for_remote_meter_points.api.serializers import UserApiSerializer, UserCreateApiSerializer, \
    SIMApiSerializer, \
    SIMCreateApiSerializer, ModemApiSerializer, ModemCreateApiSerializer, MeterDeviceApiSerializer, \
    MeterDeviceCreateApiSerializer, TaskApiSerializer, TaskCreateApiSerializer, MeterPointApiSerializer, \
    MeterPointCreateApiSerializer
from system_for_remote_meter_points.meter_devices.models import MeterDevice
from system_for_remote_meter_points.meter_points.models import MeterPoint
from system_for_remote_meter_points.modems.models import Modem
from system_for_remote_meter_points.tasks.models import Task

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
        super().post(*args, **kwargs)
        return redirect('list users api')


class UserUpdateApiView(rest_views.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserApiSerializer
    lookup_field = 'pk'

    def put(self, *args, **kwargs):
        super().put(*args, **kwargs)
        serializer = UserApiSerializer(UserModel.objects.all(), many=True)
        return Response(serializer.data)


class UserDeleteApiView(rest_views.RetrieveDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserApiSerializer
    lookup_field = 'pk'

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        serializer = UserApiSerializer(UserModel.objects.all(), many=True)
        return Response(serializer.data)


class SIMListApiView(rest_views.ListAPIView):
    queryset = SIM.objects.all()
    serializer_class = SIMApiSerializer


class SIMCreateApiView(rest_views.ListCreateAPIView):
    queryset = SIM.objects.all()
    serializer_class = SIMCreateApiSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('list sims api')


class SIMUpdateApiView(rest_views.RetrieveUpdateAPIView):
    queryset = SIM.objects.all()
    serializer_class = SIMApiSerializer
    lookup_field = 'pk'

    def put(self, *args, **kwargs):
        super().put(*args, **kwargs)
        serializer = SIMApiSerializer(SIM.objects.all(), many=True)
        return Response(serializer.data)


class SIMDeleteApiView(rest_views.RetrieveDestroyAPIView):
    queryset = SIM.objects.all()
    serializer_class = SIMApiSerializer
    lookup_field = 'pk'

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        serializer = SIMApiSerializer(SIM.objects.all(), many=True)
        return Response(serializer.data)


class ModemListApiView(rest_views.ListAPIView):
    queryset = Modem.objects.all()
    serializer_class = ModemApiSerializer


class ModemCreateApiView(rest_views.ListCreateAPIView):
    queryset = Modem.objects.all()
    serializer_class = ModemCreateApiSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('list modems api')


class ModemUpdateApiView(rest_views.RetrieveUpdateAPIView):
    queryset = Modem.objects.all()
    serializer_class = ModemApiSerializer
    lookup_field = 'pk'

    def put(self, *args, **kwargs):
        super().put(*args, **kwargs)
        serializer = ModemApiSerializer(Modem.objects.all(), many=True)
        return Response(serializer.data)


class ModemDeleteApiView(rest_views.RetrieveDestroyAPIView):
    queryset = Modem.objects.all()
    serializer_class = ModemApiSerializer
    lookup_field = 'pk'

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        serializer = ModemApiSerializer(Modem.objects.all(), many=True)
        return Response(serializer.data)


class MeterDeviceListApiView(rest_views.ListAPIView):
    queryset = MeterDevice.objects.all()
    serializer_class = MeterDeviceApiSerializer


class MeterDeviceCreateApiView(rest_views.ListCreateAPIView):
    queryset = MeterDevice.objects.all()
    serializer_class = MeterDeviceCreateApiSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('list meter devices api')


class MeterDeviceUpdateApiView(rest_views.RetrieveUpdateAPIView):
    queryset = MeterDevice.objects.all()
    serializer_class = MeterDeviceApiSerializer
    lookup_field = 'pk'

    def put(self, *args, **kwargs):
        super().put(*args, **kwargs)
        serializer = MeterDeviceApiSerializer(MeterDevice.objects.all(), many=True)
        return Response(serializer.data)


class MeterDeviceDeleteApiView(rest_views.RetrieveDestroyAPIView):
    queryset = MeterDevice.objects.all()
    serializer_class = MeterDeviceApiSerializer
    lookup_field = 'pk'

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        serializer = MeterDeviceApiSerializer(MeterDevice.objects.all(), many=True)
        return Response(serializer.data)


class TaskListApiView(rest_views.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskApiSerializer


class TaskCreateApiView(rest_views.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateApiSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('list tasks api')


class TaskUpdateApiView(rest_views.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskApiSerializer
    lookup_field = 'pk'

    def put(self, *args, **kwargs):
        super().put(*args, **kwargs)
        serializer = TaskApiSerializer(Task.objects.all(), many=True)
        return Response(serializer.data)


class TaskDeleteApiView(rest_views.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskApiSerializer
    lookup_field = 'pk'

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        serializer = TaskApiSerializer(Task.objects.all(), many=True)
        return Response(serializer.data)


class MeterPointListApiView(rest_views.ListAPIView):
    queryset = MeterPoint.objects.all()
    serializer_class = MeterPointApiSerializer


class MeterPointCreateApiView(rest_views.ListCreateAPIView):
    queryset = MeterPoint.objects.all()
    serializer_class = MeterPointCreateApiSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('list meter points api')


class MeterPointUpdateApiView(rest_views.RetrieveUpdateAPIView):
    queryset = MeterPoint.objects.all()
    serializer_class = MeterPointApiSerializer
    lookup_field = 'pk'

    def put(self, *args, **kwargs):
        super().put(*args, **kwargs)
        serializer = MeterPointApiSerializer(MeterPoint.objects.all(), many=True)
        return Response(serializer.data)


class MeterPointDeleteApiView(rest_views.RetrieveDestroyAPIView):
    queryset = MeterPoint.objects.all()
    serializer_class = MeterPointApiSerializer
    lookup_field = 'pk'

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        serializer = MeterPointApiSerializer(MeterPoint.objects.all(), many=True)
        return Response(serializer.data)
