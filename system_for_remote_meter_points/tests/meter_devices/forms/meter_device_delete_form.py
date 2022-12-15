from django.test import TestCase

from system_for_remote_meter_points.meter_devices.forms import DeleteMeterDeviceForm


class DeleteMeterDeviceFormTests(TestCase):
    def test_delete_meter_device_form_disabled_fields__when_all__expect_ok(self):
        form = DeleteMeterDeviceForm()
        disabled_fields = {
            name: field.widget.attrs[DeleteMeterDeviceForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            DeleteMeterDeviceForm.disabled_attr_name,
            disabled_fields['meter_device_number'],
        )
        self.assertEqual(
            DeleteMeterDeviceForm.disabled_attr_name,
            disabled_fields['meter_device_type'],
        )
        self.assertEqual(
            DeleteMeterDeviceForm.disabled_attr_name,
            disabled_fields['meter_device_read_cycle'],
        )
        self.assertEqual(
            DeleteMeterDeviceForm.disabled_attr_name,
            disabled_fields['user'],
        )

    def test_delete_meter_device_form_disabled_fields__when_meter_device_number_is_disabled__expect_meter_device_number_to_be_disabled(self):
        DeleteMeterDeviceForm.disabled_fields = ('meter_device_number',)
        form = DeleteMeterDeviceForm()
        disabled_fields = {
            name: field.widget.attrs[DeleteMeterDeviceForm.disabled_attr_name]
            for name, field in form.fields.items()
            if DeleteMeterDeviceForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            DeleteMeterDeviceForm.disabled_attr_name,
            disabled_fields['meter_device_number'],
        )
        self.assertEqual(1, len(disabled_fields))