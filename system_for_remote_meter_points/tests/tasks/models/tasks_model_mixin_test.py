from django.core.exceptions import ValidationError
from django.test import TestCase

from system_for_remote_meter_points.tasks.models import Task


class AppUserModelTest(TestCase):

    def test_task_save__when_model_mixin_is_valid__expect_ok(self):

        # Arrange
        task = Task(
            mp_name="Taner Ismail",
            constant=50,
            voltage='Low',
            regional_center='Varna',
            operation='Restore communication',
            result_operation='Successful communication',
            comment='test comment',
            modem='111111',
            meter_device='1127031900000022',
            username='taner_mutalip',
        )

        # Act
        task.full_clean()  # Call this for validation
        task.save()

        # Assert
        self.assertIsNotNone(task.pk)

    def test_task_save__when_model_mixin_is_not_valid__expect_nothing(self):
        # Arrange
        task = Task(
            mp_name="Taner Ismail",
            constant=50,
            voltage='Low',
            regional_center='Varna',
            operation='Restore communication',
            result_operation='Wrong communication',
            comment='test comment',
            modem='111111',
            meter_device='1127031900000022',
            username='taner_mutalip',
        )

        with self.assertRaises(ValidationError) as context:
            task.full_clean()
            task.save()

        self.assertIsNotNone(context.exception)