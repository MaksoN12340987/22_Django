from django.contrib import admin  # type: ignore

from .models import Category, Product, Users


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "category",
    )
    list_filter = (
        "price",
        "category",
    )
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "birthday",
    )
    list_filter = (
        "surname",
        "surname",
        "birthday",
        "updated_at",
    )
    search_fields = ("name",)
