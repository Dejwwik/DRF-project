from .views import product_detail_view, product_create_view
from django.urls import path

urlpatterns = [
    path("<pk>/", product_detail_view, name="product_detail"),
    path("", product_create_view, name="product_create")
]
