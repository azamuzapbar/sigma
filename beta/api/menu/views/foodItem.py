from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from apps.menu.models import FoodItem
from api.menu.serializers import FoodItemSerializer
from rest_framework.permissions import IsAuthenticated


@extend_schema(tags=["fooditems"])
class FoodItemViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer