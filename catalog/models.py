from django.db import models


class Product(models.Model):
    
    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"
        ordering = ["last_name"]



class Category(models.Model):
    
    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"
        ordering = ["last_name"]



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
