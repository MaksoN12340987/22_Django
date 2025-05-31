from django.contrib import admin

from .models import Category, Product


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
