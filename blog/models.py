from django.db import models
from users.models import BaseUser


class Posts(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок", unique=True)
    content = models.TextField(null=True, blank=True, verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="posts/",
        verbose_name="Фотография",
        null=True,
    )
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    publication_flag = models.BooleanField(verbose_name="Видно всем?", default=False)
    number_views = models.IntegerField(
        help_text="Количество просмотров",
        verbose_name="Количество просмотров",
        blank=True,
        default=0,
    )

    def __str__(self) -> str:
        return f"{self.title} {self.content}"
    

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["title"]
        permissions = [("add_comments", "You can leave a comment")]
