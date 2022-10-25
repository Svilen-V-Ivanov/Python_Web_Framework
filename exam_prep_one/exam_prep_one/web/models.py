from django.core import validators, exceptions
from django.db import models

'''
⦁	Profile
⦁	Username
⦁	Email
⦁	Email field, required.
⦁	Age
⦁	Integer field, optional.
⦁	The age cannot be below 0.

'''


def username_validator(value):
    for x in value:
        if not x.isalnum() and x != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    CHAR_MAX_LEN = 15
    CHAR_MIN_LEN = 2
    username = models.CharField(
        max_length=CHAR_MAX_LEN,
        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(CHAR_MIN_LEN),
            username_validator,
        ),
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME = 30
    MAX_GENRE_NAME = 30
    MIN_PRICE = 0.0

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    DANCE_MUSIC = 'Dance Music'
    OTHER_MUSIC = 'Other'

    MUSIC = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    album_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_NAME,
        blank=False,
        null=False,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_NAME,
        blank=False,
        null=False,
        choices=MUSIC,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        ),
    )

    class Meta:
        ordering = ('pk', )
