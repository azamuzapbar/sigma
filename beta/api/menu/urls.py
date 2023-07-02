
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.menu import MenuViewSet

from .views.category import CategoryViewSet

from .views.foodItem import FoodItemViewSet

router = DefaultRouter()

router.register("", MenuViewSet, basename="menu")
router.register("category", CategoryViewSet, basename="menu_category")
router.register("fooditems", FoodItemViewSet, basename="fooditems")


urlpatterns = [
    path("", include(router.urls)),
]