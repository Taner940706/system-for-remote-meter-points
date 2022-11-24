from django import forms

from system_for_remote_meter_points.modems.models import Modem


class ModemBaseForm(forms.ModelForm):
    class Meta:
        model = Modem
        fields = ('modem_number', 'meter_point', 'sim')


class CreateModemForm(forms.ModelForm):
    pass


class EditModemForm(ModemBaseForm):
    pass


class DeleteModemForm(ModemBaseForm):
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