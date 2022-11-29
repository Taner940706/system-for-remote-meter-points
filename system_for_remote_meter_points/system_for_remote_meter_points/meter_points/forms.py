from django import forms

from system_for_remote_meter_points.meter_points.models import MeterPoint


class MeterPointBaseForm(forms.ModelForm):
    class Meta:
        model = MeterPoint
        fields = ('mp_name', 'constant', 'voltage', 'regional_center', 'operation', 'result_operation', 'comment', 'user', 'meter_device', 'modem')
        labels = {
            'mp_name': 'Meter point name:',
            'meter_device': 'Meter device number:',
            'voltage': 'Voltage:',
            'constant': 'Constant:',
            'regional_center': 'Regional center:',
            'modem': 'Modem number:',
            'operation': 'Operation:',
            'result_operation': 'Result:',
        }
        widgets = {
            'mp_name': forms.TextInput(
                attrs={
                    'placeholder': 'Meter point name',

                }

            ),
            'meter_device': forms.TextInput(
                attrs={
                    'placeholder': 'Meter device number',
                }

            ),

            'constant': forms.NumberInput(

            ),

            'modem': forms.TextInput(
                attrs={
                    'placeholder': 'Modem number',
                }

            ),
            'user': forms.TextInput(
                attrs={
                    'placeholder': 'User name',
                }


            ),


        }


class CreateMeterPointForm(MeterPointBaseForm):
    pass


class EditMeterPointForm(MeterPointBaseForm):
    pass


class DeleteMeterPointForm(MeterPointBaseForm):
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