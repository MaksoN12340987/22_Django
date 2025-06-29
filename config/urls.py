from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from blog.apps import BlogConfig
from catalog.apps import CatalogConfig
from users.apps import UsersConfig

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{BlogConfig.name}/", include(f"{BlogConfig.name}.urls", namespace=f"{BlogConfig.name}",)),
    path(f"{UsersConfig.name}/", include(f"{UsersConfig.name}.urls", namespace=f"{UsersConfig.name}",)),
    path(f"{CatalogConfig.name}/", include(f"{CatalogConfig.name}.urls", namespace=f"{CatalogConfig.name}")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
