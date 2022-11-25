from django import forms
from system_for_remote_meter_points.tasks.models import Task


class TaskBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('mp_name', 'constant', 'voltage', 'regional_center', 'modem_number', 'ip_address', 'operation', 'result_operation', 'comment')


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