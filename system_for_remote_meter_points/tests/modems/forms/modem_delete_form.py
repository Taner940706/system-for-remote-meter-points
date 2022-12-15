from django.test import TestCase

from system_for_remote_meter_points.modems.forms import DeleteModemForm


class DeleteModemFormTests(TestCase):
    def test_delete_modem_form_disabled_fields__when_all__expect_ok(self):
        form = DeleteModemForm()
        disabled_fields = {
            name: field.widget.attrs[DeleteModemForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            DeleteModemForm.disabled_attr_name,
            disabled_fields['modem_number'],
        )
        self.assertEqual(
            DeleteModemForm.disabled_attr_name,
            disabled_fields['sim'],
        )
        self.assertEqual(
            DeleteModemForm.disabled_attr_name,
            disabled_fields['user'],
        )

    def test_modem_delete_form_disabled_fields__when_modem_number_is_disabled__expect_modem_number_to_be_disabled(self):
        DeleteModemForm.disabled_fields = ('modem_number',)
        form = DeleteModemForm()
        disabled_fields = {
            name: field.widget.attrs[DeleteModemForm.disabled_attr_name]
            for name, field in form.fields.items()
            if DeleteModemForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            DeleteModemForm.disabled_attr_name,
            disabled_fields['modem_number'],
        )
        self.assertEqual(1, len(disabled_fields))