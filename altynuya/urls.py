from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Altyn-Uya API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url='https://altynuya.kg'
)

urlpatterns = [
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/admin/', admin.site.urls),
    path('api/user/', include('apps.user.urls')),
    path('api/', include('apps.news.urls')),
    path('api/', include('apps.gallery.urls')),
    path('api/', include('apps.teachers.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

