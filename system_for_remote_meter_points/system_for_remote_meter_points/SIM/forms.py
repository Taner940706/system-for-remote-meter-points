from django import forms

from system_for_remote_meter_points.SIM.models import SIM


class SIMBaseForm(forms.ModelForm):
    class Meta:
        model = SIM
        fields = ('sim_number', 'gsm_number', 'ip_address', 'operator', 'modem')


class CreateSIMForm(SIMBaseForm):
    pass


class EditSIMForm(SIMBaseForm):
    pass


class DeleteSIMForm(SIMBaseForm):
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