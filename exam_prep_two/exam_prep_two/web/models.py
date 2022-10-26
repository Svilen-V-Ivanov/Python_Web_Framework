from django.core import validators
from django.db import models


class Profile(models.Model):
    MIN_AGE_VALUE = 12
    MAX_LEN_PASSWORD = 30
    MAX_LEN_NAME = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_AGE_VALUE),
        )
    )
    #TODO: make this a password field in form
    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_PASSWORD,

    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_NAME,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_NAME,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )


class Game(models.Model):
    MAX_LEN_TITLE = 30
    MAX_LEN_CATEGORY = 15
    MIN_GAME_RATING = 0.1
    MAX_GAME_RATING = 5.0
    MIN_LEVEL = 1

    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'

    GAMES = (
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER, OTHER),
    )

    title = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=MAX_LEN_TITLE,
    )

    category = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_CATEGORY,
        choices=GAMES,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_GAME_RATING),
            validators.MaxValueValidator(MAX_GAME_RATING),
        )
    )

    max_level = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=(
            validators.MinValueValidator(MIN_LEVEL),
        )
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )