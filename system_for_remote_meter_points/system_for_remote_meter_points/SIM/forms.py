from django import forms

from system_for_remote_meter_points.SIM.models import SIM
from system_for_remote_meter_points.core.form_mixins import DisabledFormMixin


class SIMBaseForm(forms.ModelForm):
    class Meta:
        model = SIM
        fields = ('sim_number', 'gsm_number', 'ip_address', 'operator', 'user')
        labels = {
            'sim_number': 'SIM number:',
            'gsm_number': 'GSM number:',
            'ip_address': 'IP address:',
            'operator': 'Operator:',

        }
        widgets = {
            'sim_number': forms.TextInput(
                attrs={
                    'placeholder': 'SIM Number',

                }

            ),
            'gsm_number': forms.TextInput(
                attrs={
                    'placeholder': 'GSM Number',
                }

            ),
            'ip_address': forms.TextInput(
                attrs={
                    'placeholder': 'IP address',
                }

            ),
            'user': forms.TextInput(
                attrs={
                    'placeholder': 'User name',
                }

            ),
        }


class CreateSIMForm(SIMBaseForm):
    pass


class EditSIMForm(SIMBaseForm):
    pass


class DeleteSIMForm(SIMBaseForm, DisabledFormMixin):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance