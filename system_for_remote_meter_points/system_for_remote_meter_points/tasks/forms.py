from django import forms

from system_for_remote_meter_points.core.form_mixins import DisabledFormMixin
from system_for_remote_meter_points.tasks.models import Task


class TaskBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('mp_name', 'constant', 'voltage', 'regional_center', 'operation', 'result_operation', 'comment', 'meter_device', 'modem')
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
        # widgets = {
        #     'mp_name': forms.CharField(
        #
        #
        #     ),
        #     'meter_device': forms.CharField(
        #
        #     ),
        #     'voltage': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Voltage',
        #         }
        #     ),
        #     'constant': forms.NumberInput(
        #
        #     ),
        #     'regional_center': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Regional center',
        #         }
        #
        #     ),
        #     'modem': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Modem number',
        #         }
        #
        #     ),
        #     'operation': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Operation',
        #         }
        #
        #     ),
        #     'result_operation': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Result',
        #         }
        #
        #     ),
        #
        # }



class EditTaskForm(TaskBaseForm):
    pass


class DeleteTaskForm(TaskBaseForm, DisabledFormMixin):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance