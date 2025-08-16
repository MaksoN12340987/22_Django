from django.contrib import admin  # type: ignore

from .models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "creation_date",
        "publication_flag",
        "number_views",
    )
    list_filter = (
        "publication_flag",
        "creation_date",
    )
    search_fields = ("title",)
