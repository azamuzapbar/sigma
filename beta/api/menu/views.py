from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from apps.menu.models import Menu
from api.menu.serializers import MenuSerializer
from rest_framework.permissions import IsAuthenticated


@extend_schema(tags=["menu"])
class MenuViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
