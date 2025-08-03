import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CreateForm, UpdateProduct
from .models import Product

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
        data = form.cleaned_data

        if not data["on_sale"]:
            if not self.permission_user:
                return HttpResponseForbidden(
                    "У вас нет прав для удаления или снятия с продажи этого продукта."
                )

        return super().form_valid(form)


class ProductCategoriesListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/catalog.html"
    context_object_name = "products"


class OrdersView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/orders.html"
    context_object_name = "products"


class OrdersDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/orders_delite.html"
    success_url = reverse_lazy("catalog:orders")

    def post(self, request, *args, **kwargs) -> HttpResponse:
        if not request.user.has_perm("catalog.delite_product"):
            return HttpResponseForbidden("У вас нет прав для удаления этого продукта.")
        obj = self.get_object()
        if not obj.owner == self.request.user: # type: ignore
            return HttpResponseForbidden("У вас нет прав для удаления этого продукта.")

        return super().post(request, *args, **kwargs)


class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    form_class = CreateForm
    template_name = "catalog/create.html"
    success_url = reverse_lazy("catalog:catalog")

    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.permission_user = request.user.has_perm("catalog.can_unpublish_product")
        self.user_id = request.user.id  # type: ignore
        logger_views.info(self.user_id)

        return super().post(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        data = form.cleaned_data
        logger_views.info(data)

        if not data["on_sale"]:
            if not self.permission_user:
                return HttpResponseForbidden(
                    "У вас нет прав для удаления или снятия с продажи этого продукта."
                )
        elif data["owner"].id != self.user_id:
            return HttpResponseForbidden(
                """<div class="container-fluid-base text-start">
                        <h1 class="ms-5 mt-5 p-5">Укажите, в поле "Владелец" автором себя</h1>
                        </div>"""
            )

        return super().form_valid(form)
