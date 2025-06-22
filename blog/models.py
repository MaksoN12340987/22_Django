from django.db import models  # type: ignore

# from PIL import Image # type: ignore
from config.settings import MEDIA_ROOT  # type: ignore


class Posts(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок", unique=True)
    content = models.TextField(null=True, blank=True, verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog/", verbose_name="Фотография", null=True, blank=True
    )
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    publication_flag = models.BooleanField(
        help_text="Признак", verbose_name="Признак", default=False
    )
    number_views = models.PositiveIntegerField(
        help_text="Количество просмотров",
        verbose_name="Количество просмотров",
        blank=True,
        default=0,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["title"]
