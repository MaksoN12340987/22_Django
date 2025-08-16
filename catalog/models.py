from django.db import models

from users.models import BaseUser

# from catalog.models import Product, Category


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование", unique=True)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование", unique=True)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="photos/", verbose_name="Фотография", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="categories",
        max_length=200,
        verbose_name="Категория",
    )
    price = models.IntegerField(verbose_name="Цена")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        null=True, verbose_name="Дата последнего изменения", auto_now=True
    )
    on_sale = models.BooleanField(default=True)
    owner = models.ForeignKey(
        BaseUser,
        on_delete=models.CASCADE,
        related_name="owner",
        max_length=200,
        verbose_name="Владелец",
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name} {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
        permissions = [
            # можно отменить публикацию продукта
            ("can_unpublish_product", "Can unpublish product"),
        ]
