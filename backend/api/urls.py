from django.urls import include, path
from rest_framework import routers

from api.views import TagViewSet, IngredientViewSet, RecipeViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register(
    r'tag',
    TagViewSet,
    basename='tag',
)
router.register(
    r'ingredients',
    IngredientViewSet,
    basename='ingredients',
)
router.register(
    r'recipes',
    RecipeViewSet,
    basename='recipes',
)

urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
