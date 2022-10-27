from django.db import models


class Profile(models.Model):
    MAX_NAME_LENGTH = 30

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_NAME_LENGTH,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_NAME_LENGTH,
        verbose_name='Last Name'
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )


class Book(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_TYPE_LENGTH = 30

    title = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_TITLE_LENGTH,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_TYPE_LENGTH,
    )

    class Meta:
        ordering = ('pk',)
