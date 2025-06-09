from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore

from blog.apps import BlogProjectName
from catalog.apps import CatalogProjectConfig

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        f"{CatalogProjectConfig.name}/",
        include(
            f"{CatalogProjectConfig.name}.urls",
            namespace=f"{CatalogProjectConfig.name}",
        ),
    ),
    path(
        f"{BlogProjectName.name}/",
        include(
            f"{BlogProjectName.name}.urls",
            namespace=f"{BlogProjectName.name}",
        ),
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
