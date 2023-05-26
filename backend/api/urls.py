from django.urls import include, path
from rest_framework import routers

from api.views import TagViewSet, IngredientViewSet, RecipeViewSet, FollowViewSet

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
    path('users/subscriptions/', FollowViewSet.as_view({'get': 'list'}), name='subscriptions'),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('', include(router.urls)),
]
