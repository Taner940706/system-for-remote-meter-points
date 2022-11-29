from django import forms

from system_for_remote_meter_points.meter_devices.models import MeterDevice


class MeterDeviceBaseForm(forms.ModelForm):
    class Meta:
        model = MeterDevice
        fields = ('meter_device_number', 'meter_device_type', 'meter_device_read_cycle', 'user')
        labels = {
            'meter_device_number': 'Meter device number:',
            'meter_device_type': 'Meter device type:',
            'meter_device_read_cycle': 'Select read cycle:'

        }
        widgets = {
            'meter_device_number': forms.TextInput(
                attrs={
                    'placeholder': 'Meter device number',

                }

            ),
            'user': forms.TextInput(
                attrs={
                    'placeholder': 'User name',
                }

            ),

        }

class CreateMeterDeviceForm(MeterDeviceBaseForm):
    pass


class EditMeterDeviceForm(MeterDeviceBaseForm):
    pass


class DeleteMeterDeviceForm(MeterDeviceBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'