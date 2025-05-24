from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    
    age = models.IntegerField()
    is_activ = models.BooleanField(default=True)
    descripyion = models.TextField(null=True, blank=True)\
        # null — определяет, может ли поле принимать значение NULL
        # blank — определяет, может ли поле быть пустым в формах. Полезно для валидации данных.
    create_at = models.DateTimeField()
    
    image = models.ImageField()
    
    # Зависимость данных один ко многим
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    # Один к одному
    profils = models.OneToOneField(Profile, on_delete=models.CASCADE)
    
    # Многие ко многим
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ['last_name']
