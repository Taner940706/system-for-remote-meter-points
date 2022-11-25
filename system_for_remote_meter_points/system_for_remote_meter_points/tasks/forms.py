from django import forms
from system_for_remote_meter_points.tasks.models import Task


class TaskBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('mp_name', 'constant', 'voltage', 'regional_center', 'modem_number', 'ip_address', 'operation', 'result_operation', 'comment', 'meter_device_number')
        labels = {
            'mp_name': 'Meter point name:',
            'meter_device_number': 'Meter device number:',
            'voltage': 'Voltage:',
            'constant': 'Constant:',
            'regional_center': 'Regional center:',
            'modem_number': 'Modem number:',
            'ip_address': 'IP address:',
            'operation': 'Operation:',
            'result_operation': 'Result:',

        }
        widgets = {
            'mp_name': forms.TextInput(
                attrs={
                    'placeholder': 'Meter point name',

                }

            ),
            'meter_device_number': forms.TextInput(
                attrs={
                    'placeholder': 'Meter device number',
                }

            ),
            'voltage': forms.TextInput(
                attrs={
                    'placeholder': 'Voltage',
                }
            ),
            'constant': forms.TextInput(
                attrs={
                    'placeholder': 'Constant',
                }

            ),
            'regional_center': forms.TextInput(
                attrs={
                    'placeholder': 'Regional center',
                }

            ),
            'modem_number': forms.TextInput(
                attrs={
                    'placeholder': 'Modem number',
                }

            ),
            'ip_address': forms.TextInput(
                attrs={
                    'placeholder': 'IP address',
                }

            ),
            'operation': forms.TextInput(
                attrs={
                    'placeholder': 'Operation',
                }

            ),
            'result_operation': forms.TextInput(
                attrs={
                    'placeholder': 'Result',
                }

            ),
        }


class EditTaskForm(TaskBaseForm):
    pass


class DeleteTaskForm(TaskBaseForm):
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