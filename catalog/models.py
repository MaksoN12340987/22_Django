from django.db import models


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
    last_name = models.CharField(max_length=150, verbose_name="Afvbkbz")
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

    # first_name = models.CharField(max_length=150, verbose_name='Имя')
    # last_name = models.CharField(max_length=150, verbose_name='Фамилия')

    # age = models.IntegerField( help_text="Введите возвраст")
    # is_activ = models.BooleanField(default=True)
    # descripyion = models.TextField(null=True, blank=True)\
    #     # null — определяет, может ли поле принимать значение NULL
    #     # blank — определяет, может ли поле быть пустым в формах. Полезно для валидации данных.
    # create_at = models.DateTimeField(auto_now_add=True)

    # image = models.ImageField(upload_to='photos/', verbose_name='Фотография')

    # # Зависимость данных один ко многим
    # group = models.ForeignKey(Group, on_delete=models.CASCADE)

    # # Один к одному
    # profils = models.OneToOneField(Profile, on_delete=models.CASCADE)

    # # Многие ко многим
    # tags = models.ManyToManyField(Tag)

    # STATUS_CHOICES = [
    #     ('draft', 'Draft')
    #     ('published', 'Published')
    # ]
    # status = models.CharField()

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'
