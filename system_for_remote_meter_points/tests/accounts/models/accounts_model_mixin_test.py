from django.core.exceptions import ValidationError
from django.test import TestCase

from system_for_remote_meter_points.accounts.models import AppUser


class AppUserModelTest(TestCase):

    def test_appuser_save__when_model_mixin_is_valid__expect_ok(self):

        # Arrange
        profile = AppUser(
            username="taner940706",
            password="testtaner940706",
            first_name='Taner',
            last_name='Ismail',
            email='taner@email.com',
            department='DOSO',
            picture='user_photos/5-Ways-to-Analyze-Employee-Performance-1024x508.jpg',
        )

        # Act
        profile.full_clean()  # Call this for validation
        profile.save()

        # Assert
        self.assertIsNotNone(profile.pk)

    def test_appuser_save__when_model_mixin_is_not_valid__expect_nothing(self):
        # Arrange
        profile = AppUser(
            username="taner940706",
            password="testtaner940706",
            first_name='Taner',
            last_name='Ismail',
            email='taner@email.com',
            department='KMU',
            picture='user_photos/5-Ways-to-Analyze-Employee-Performance-1024x508.jpg',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)