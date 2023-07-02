from io import BytesIO
import qrcode
from django.http import HttpResponse
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets
from apps.restaurant.models import Restaurant
from api.restaurant.serializers import RestaurantSerializer

@extend_schema_view(
    list=extend_schema(tags=["restaurant"]),
    generate_qr_code=extend_schema(tags=["restaurant"])
                    )
class RestaurantViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(methods=["GET"], detail=True)
    def generate_qr_code(self, request, pk=None):
        restaurant = self.get_object()
        qr_code_url = f'azamuzapbar.pythonanywhere.com/menu/{restaurant.pk}/'
        qr_code = qrcode.make(qr_code_url)

        buffer = BytesIO()
        qr_code.save(buffer)
        qr_code_img = buffer.getvalue()
        buffer.close()

        return HttpResponse(qr_code_img, content_type='image/png')