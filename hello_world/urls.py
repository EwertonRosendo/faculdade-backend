from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from hello_world.core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("", include('backend.urls')),
    path("api/schema/", SpectacularAPIView.as_view(),name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
