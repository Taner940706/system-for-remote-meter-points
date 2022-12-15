from django.test import TestCase

from system_for_remote_meter_points.meter_points.forms import DeleteMeterPointForm


class DeleteMeterPointFormTests(TestCase):
    def test_delete_meter_point_form_disabled_fields__when_all__expect_ok(self):
        form = DeleteMeterPointForm()
        disabled_fields = {
            name: field.widget.attrs[DeleteMeterPointForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['mp_name'],
        )
        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['constant'],
        )
        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['voltage'],
        )
        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['regional_center'],
        )
        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['operation'],
        )
        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['result_operation'],
        )
        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['comment'],
        )
        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['user'],
        )
        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['meter_device'],
        )
        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['modem'],
        )

    def test_meter_point_form_disabled_fields__when_meter_point_name_is_disabled__expect_meter_point_name_to_be_disabled(self):
        DeleteMeterPointForm.disabled_fields = ('mp_name',)
        form = DeleteMeterPointForm()
        disabled_fields = {
            name: field.widget.attrs[DeleteMeterPointForm.disabled_attr_name]
            for name, field in form.fields.items()
            if DeleteMeterPointForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            DeleteMeterPointForm.disabled_attr_name,
            disabled_fields['mp_name'],
        )
        self.assertEqual(1, len(disabled_fields))