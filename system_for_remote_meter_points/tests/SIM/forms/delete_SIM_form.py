from django.test import TestCase

from system_for_remote_meter_points.SIM.forms import DeleteSIMForm


class DeleteSIMFormTests(TestCase):
    def test_delete_SIM_form_disabled_fields__when_all__expect_ok(self):
        form = DeleteSIMForm()
        disabled_fields = {
            name: field.widget.attrs[DeleteSIMForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            DeleteSIMForm.disabled_attr_name,
            disabled_fields['sim_number'],
        )
        self.assertEqual(
            DeleteSIMForm.disabled_attr_name,
            disabled_fields['gsm_number'],
        )
        self.assertEqual(
            DeleteSIMForm.disabled_attr_name,
            disabled_fields['ip_address'],
        )
        self.assertEqual(
            DeleteSIMForm.disabled_attr_name,
            disabled_fields['operator'],
        )
        self.assertEqual(
            DeleteSIMForm.disabled_attr_name,
            disabled_fields['user'],
        )

    def test_delete_SIM_form_disabled_fields__when_sim_number_is_disabled__expect_sim_number_to_be_disabled(self):
        DeleteSIMForm.disabled_fields = ('sim_number',)
        form = DeleteSIMForm()
        disabled_fields = {
            name: field.widget.attrs[DeleteSIMForm.disabled_attr_name]
            for name, field in form.fields.items()
            if DeleteSIMForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            DeleteSIMForm.disabled_attr_name,
            disabled_fields['sim_number'],
        )
        self.assertEqual(1, len(disabled_fields))