from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from apps.menu.models import Category
from api.menu.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated


@extend_schema(tags=["menu_category"])
class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer