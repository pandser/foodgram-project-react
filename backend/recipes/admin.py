from django.contrib import admin

from recipes.models import (Favorite, Follow, Ingredient, IngredientsInRecipes,
                            Recipe, ShoppingCart, Tag)


@admin.register(IngredientsInRecipes)
class IngredientsInRecipesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'amount',
        'recipe',
        'ingredient',
    )


class IngredientsInRecipesInline(admin.TabularInline):
    model = IngredientsInRecipes


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'author',
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit',
    )
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'name',
        'pub_date',
        'text',
        'cooking_time',
        'image',
        'favorite_count',
    )
    inlines = (IngredientsInRecipesInline,)
    list_filter = ('name', 'author', 'tags')

    def favorite_count(self, obj):
        return obj.favorite.count()

    favorite_count.short_description = 'В избранном'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'slug',
    )
