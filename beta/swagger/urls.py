from django.urls import path
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularAPIView,
)

swagger_patterns = [
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
]