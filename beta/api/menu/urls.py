from api.menu.views import MenuViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("", MenuViewSet, basename="menu")

urlpatterns = [
    path("", include(router.urls)),
]