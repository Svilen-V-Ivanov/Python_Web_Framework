from django.db import models

from forms_validations.web.validators import validate_text, ValueInRangeValidator


class Person(models.Model):
    MAX_LEN_NAME = 20

    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='persons',
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    MAX_TODOS_PER_PERSON = 3
    MAX_LEN_TEXT = 25
    text = models.CharField(
        max_length=MAX_LEN_TEXT,
        validators=(
            validate_text,
        ),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    assignee = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )