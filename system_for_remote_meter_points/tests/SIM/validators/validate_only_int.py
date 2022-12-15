from unittest import TestCase

from django.core.exceptions import ValidationError

from system_for_remote_meter_points.core.validators import only_int


class OnlyIntValidator(TestCase):
    def test_only_digits_validator__when_valid__expect_ok(self):
        only_int('5465462682')

    def test_only_digits_validator__when_contains_letters__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            only_int('Taner940706')
        self.assertIsNotNone(context.exception)
