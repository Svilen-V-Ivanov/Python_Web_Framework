from django.db import models


class Profile(models.Model):
    MAX_NAME_LEN = 20
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_NAME_LEN,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_NAME_LEN,
        verbose_name='Last Name',
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )


class Note(models.Model):
    MAX_CHAR_NAME = 30

    title = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_CHAR_NAME,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    content = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('pk',)
