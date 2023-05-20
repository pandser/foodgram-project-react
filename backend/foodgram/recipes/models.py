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
        verbose_name='Ингредиент',
    )
    measurement_unit = models.CharField(
        max_length=30,
        verbose_name='Еденица измерения'
    )

    def __str__(self):
        return self.name


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
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    text = models.TextField(
        verbose_name='Описание',
    )
    tags = ArrayField(
        models.PositiveIntegerField(),
        blank=True,
    )
    ingredients = ArrayField(
        ArrayField(
            models.PositiveIntegerField(),
            size=2,
        ),
    )
    amount = models.ManyToManyField(
        Ingredient,
        through='IngredientsInRecipes',
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name="Время приготовления",
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='recipe/',
    )

    def __str__(self):
        return self.name


class IngredientsInRecipes(models.Model):
    """Связь рецепт ингредиент."""
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='amount_ingredient',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='amount',
    )


class Favorite(models.Model):
    """Модель избранное."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )


class ShoppingCart(models.Model):
    """Модель список покупок."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )
