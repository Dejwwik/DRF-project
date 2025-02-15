from .views import product_detail_view, product_create_list_view, product_alt_view
from django.urls import path

urlpatterns = [
    path("<pk>/", product_alt_view),
    path("", product_create_list_view, name="product_create_list")
]
