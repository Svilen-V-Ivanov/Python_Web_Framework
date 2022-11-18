# web_tests.py
from django.test import TestCase

from testing_demos.web.models import Profile


class ProfileModelTests(TestCase):
    # 3A - Arrange, Act, Assert --> SetUp, Do, Check result

    def test_profile_save__when_egn_is_valid__expect_correct_result(self):
        # Arrange
        profile = Profile(
            name='Doncho',
            age=19,
            egn='0310230467',
        )

        # Act
        profile.full_clean() # call this for validation
        profile.save()

        # Assert
        self.assertIsNotNone(profile.pk)