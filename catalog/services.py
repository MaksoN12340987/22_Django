import logging

from .models import Category

logger_services = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_services.addHandler(file_handler)
logger_services.setLevel(logging.INFO)


class AvailabilityProductModeratorRights:

    @staticmethod
    def permission_user_superuser_object(request, obj):
        """Метод проверки прав пользователя
        - может ли он удалить продукт
        - может ли он снять продукт с продажи

        Args:
            request
            obj (model): объект модели продукта

        Returns:
            str: ели прав нет
            None: если всё ок
        """
        if not request.user.has_perm("catalog.delete_product"):
            return "У вас нет права на удаление этого продукта."
        elif not request.user.is_superuser:  # type: ignore
            logger_services.info(f"пользователь не superuser")
            if not obj.owner == request.user:  # type: ignore
                return "У вас нет прав для удаления этого продукта."

    @staticmethod
    def permission_user_superuser_cleaned_data(request, data):
        """Метод проверки прав пользователя
        - может ли он удалить продукт
        - может ли он снять продукт с продажи

        Args:
            request
            form.cleaned_data: словарь формы

        Returns:
            str: ели прав нет
            None: если всё ок
        """
        if not request.user.is_superuser:  # type: ignore
            logger_services.info("пользователь не superuser")

            if not data["on_sale"] and not request.user.has_perm(
                "catalog.can_unpublish_product"
            ):
                return (
                    "У вас нет прав для удаления или снятия с продажи этого продукта."
                )


class ListProductsByCategory:

    @staticmethod
    def list_product_in_category(queryset_models, categories):
        result_list = []
        
        for category in categories:
            pass

        # for product in queryset_models:
        #     if product.category == category:
        #         result_list.append(product)
        # logger_services.info(f"{category.name} {result_list}")

        return result_list
