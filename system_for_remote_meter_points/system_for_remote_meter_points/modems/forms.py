from django import forms

from system_for_remote_meter_points.core.form_mixins import DisabledFormMixin
from system_for_remote_meter_points.modems.models import Modem


class ModemBaseForm(forms.ModelForm):
    class Meta:
        model = Modem
        fields = ('modem_number', 'sim', 'user')
        labels = {
            'modem_number': 'Modem number:',
            'sim': 'SIM number:',
        }
        widgets = {
            'modem_number': forms.TextInput(
                attrs={
                    'placeholder': 'Modem number',

                }

            ),
            'sim': forms.TextInput(
                attrs={
                    'placeholder': 'SIM number',
                }
            ),
            'user': forms.TextInput(
                attrs={
                    'placeholder': 'User name',
                }

            ),
        }


class CreateModemForm(ModemBaseForm):
    pass


class EditModemForm(ModemBaseForm):
    pass


class DeleteModemForm(ModemBaseForm, DisabledFormMixin):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
