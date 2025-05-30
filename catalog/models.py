from typing import Any
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование", unique=True)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="photos", verbose_name="Фотография", null=True)
    category = models.CharField(max_length=200, verbose_name="Категория")
    price = models.IntegerField(help_text="Цена", verbose_name="Цена")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        null=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self) -> str:
        return f"{self.name} {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]


class Category(models.Model):
    name = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="categories",
        max_length=200,
        verbose_name="Категория",
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self) -> str:
        return f"{self.name} {self.category}"

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"
        ordering = ["name"]


class Student(models.Model):
    FIRST_YEAR = "first"
    SECOND_YEAR = "second"
    THIRD_YEAR = "third"
    FOURTH_YEAR = "fourth"

    YEAR_IN_SCHOOL_CHOICES = [
        (FIRST_YEAR, "Первый курс"),
        (SECOND_YEAR, "Второй курс"),
        (THIRD_YEAR, "Третий курс"),
        (FOURTH_YEAR, "Четвертый курс"),
    ]

    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    year = models.CharField(
        max_length=10,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FIRST_YEAR,
        verbose_name="Курс",
    )

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"
        ordering = ["last_name"]
