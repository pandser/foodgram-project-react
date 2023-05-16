from django.db import models
from django.core.validators import validate_slug
from django.contrib.postgres.fields import ArrayField

from users.models import User


class Tag(models.Model):
    """Модель тэг."""

    name = models.CharField(
        max_length=200,
        verbose_name='Тэг',
    )
    color = models.CharField(
        max_length=7,
        verbose_name='Цвет в HEX',
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        validators=(validate_slug,),
        verbose_name='Уникальный слаг',
    )


class Ingredient(models.Model):
    """Модель ингредиенты."""

    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Ингредиент',
    )
    measurement_unit = models.CharField(
        max_length=30,
        verbose_name='Еденица измерения'
    )


class Recipe(models.Model):
    """Модель рецепт."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    text = models.TextField(
        verbose_name='Описание',
    )
    tags = ArrayField(
        models.ForeignKey(
            Tag,
            on_delete=models.CASCADE,
        ),
    )
    ingredients = ArrayField(
        models.ForeignKey(
            Ingredient,
            on_delete=models.CASCADE,
        ),
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name="Время приготовления",
    )
    image = models.BinaryField(
        verbose_name="Картинка",
    )
