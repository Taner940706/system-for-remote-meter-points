from django.test import TestCase

from system_for_remote_meter_points.tasks.forms import DeleteTaskForm


class DeleteTaskFormTests(TestCase):
    def test_delete_task_form_disabled_fields__when_all__expect_ok(self):
        form = DeleteTaskForm()
        disabled_fields = {
            name: field.widget.attrs[DeleteTaskForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            DeleteTaskForm.disabled_attr_name,
            disabled_fields['mp_name'],
        )
        self.assertEqual(
            DeleteTaskForm.disabled_attr_name,
            disabled_fields['constant'],
        )
        self.assertEqual(
            DeleteTaskForm.disabled_attr_name,
            disabled_fields['voltage'],
        )
        self.assertEqual(
            DeleteTaskForm.disabled_attr_name,
            disabled_fields['regional_center'],
        )
        self.assertEqual(
            DeleteTaskForm.disabled_attr_name,
            disabled_fields['operation'],
        )
        self.assertEqual(
            DeleteTaskForm.disabled_attr_name,
            disabled_fields['result_operation'],
        )
        self.assertEqual(
            DeleteTaskForm.disabled_attr_name,
            disabled_fields['comment'],
        )
        self.assertEqual(
            DeleteTaskForm.disabled_attr_name,
            disabled_fields['meter_device'],
        )
        self.assertEqual(
            DeleteTaskForm.disabled_attr_name,
            disabled_fields['modem'],
        )

    def test_delete_task_form_disabled_fields__when_meter_point_name_is_disabled__expect_meter_point_name_to_be_disabled(self):
        DeleteTaskForm.disabled_fields = ('mp_name',)
        form = DeleteTaskForm()
        disabled_fields = {
            name: field.widget.attrs[DeleteTaskForm.disabled_attr_name]
            for name, field in form.fields.items()
            if DeleteTaskForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            DeleteTaskForm.disabled_attr_name,
            disabled_fields['mp_name'],
        )
        self.assertEqual(1, len(disabled_fields))