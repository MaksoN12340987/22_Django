import json
import logging

from django.apps import AppConfig  # type: ignore

logger_app_blog = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_app_blog.addHandler(file_handler)
logger_app_blog.setLevel(logging.INFO)


class BlogProjectName(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
