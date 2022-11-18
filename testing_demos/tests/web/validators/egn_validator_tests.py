from unittest import TestCase

from django.core.exceptions import ValidationError

from testing_demos.web.validators import egn_validator


class EgnValidatorTests(TestCase):
    def test_egn_validator__when_valid__expect_ok(self):
        egn_validator('1234567890')

    def test_egn_validator__when_nine_digits__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            egn_validator('123456789')

        self.assertIsNotNone(context.exception)

    def test_egn_validator__when_eleven_digits__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            egn_validator('12345678910')

        self.assertIsNotNone(context.exception)

    def test_egn_validator__when_None__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            egn_validator('')

        self.assertIsNotNone(context.exception)

    def test_egn_validator__when_non_digit_char__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            egn_validator('123a567890')

        self.assertIsNotNone(context.exception)