import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models.base import Model as Model
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from users.models import BaseUser

from .forms import CreateForm, UpdateProduct
from .models import Product
from .services import AvailabilityProductModeratorRights

logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = cache.get("ProductListView_queryset")
        if not queryset:
            queryset = super().get_queryset()
            cache.set(
                "authors_queryset", queryset, 60 * 15
            )  # Кешируем данные на 15 минут
        return queryset


class ProductView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = UpdateProduct
    context_object_name = "product"
    template_name = "catalog/product.html"
    success_url = reverse_lazy("catalog:home")

    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.permission_user = request.user.has_perm("catalog.can_unpublish_product")
        logger_views.info(request.user.id)  # type: ignore

        return super().post(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        error = (
            AvailabilityProductModeratorRights.permission_user_superuser_cleaned_data(
                self.request, form.cleaned_data
            )
        )
        if error:
            return HttpResponseForbidden(error)

        return super().form_valid(form)


class ProductCategoriesListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/catalog.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = cache.get("ProductCategoriesListView_queryset")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("authors_queryset", queryset, 60 * 15)
        return queryset


class OrdersView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/orders.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = cache.get("OrdersView_queryset")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("authors_queryset", queryset, 60 * 15)
        return queryset


class OrdersDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/orders_delite.html"
    success_url = reverse_lazy("catalog:orders")

    def post(self, request, *args, **kwargs) -> HttpResponse:
        error = AvailabilityProductModeratorRights.permission_user_superuser_object(
            request, self.get_object()
        )
        if error:
            return HttpResponseForbidden(error)

        return super().post(request, *args, **kwargs)


class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    form_class = CreateForm
    template_name = "catalog/create.html"
    success_url = reverse_lazy("catalog:catalog")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        error = (
            AvailabilityProductModeratorRights.permission_user_superuser_cleaned_data(
                self.request, form.cleaned_data
            )
        )
        if error:
            return HttpResponseForbidden(error)

        # Привязываем текущего пользователя
        form.instance.owner = self.request.user

        return super().form_valid(form)
