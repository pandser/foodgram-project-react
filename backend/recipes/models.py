from django.core.validators import validate_slug
from django.db import models

from recipes.validators import validate_name
from users.models import User


class Tag(models.Model):
    """Модель тэг."""

    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Тэг',
    )
    color = models.CharField(
        max_length=7,
        unique=True,
        verbose_name='Цвет в HEX',
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        validators=(validate_slug,),
        verbose_name='Уникальный слаг',
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


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

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name} ,({self.measurement_unit})'


class Recipe(models.Model):
    """Модель рецепт."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    name = models.CharField(
        max_length=200,
        validators=(validate_name,),
        verbose_name='Название',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    text = models.TextField(
        verbose_name='Описание',
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тэг',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientsInRecipes',
        related_name='recipes'
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name="Время приготовления",
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='recipe/',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientsInRecipes(models.Model):
    """Связь рецепт ингредиент."""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe',
    )
    amount = models.IntegerField(
        verbose_name='Количество',
        default=1,
    )

    class Meta:
        verbose_name = 'Ингредиенты в рецептах'


class Favorite(models.Model):
    """Модель избранное."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingCart(models.Model):
    """Модель список покупок."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='cart',
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'


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

    class Meta:
        verbose_name = 'Подписки'
        verbose_name_plural = 'Подписки'
