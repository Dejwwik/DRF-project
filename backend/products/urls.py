from .views import (
    product_detail_view,
    product_create_list_view,
    product_update_view,
    product_destroy_view,
)
from django.urls import path

urlpatterns = [
    path("", product_create_list_view, name="product-list"),
    path("<pk>/", product_detail_view, name="product-detail"),
    path("<pk>/update/", product_update_view, name="product-update"),
    path("<pk>/delete/", product_destroy_view, name="product-delete"),
]
