from .views import product_detail_view, product_create_list_view, product_update_view, product_destroy_view
from django.urls import path

urlpatterns = [
    path("", product_create_list_view),
    path("<pk>/", product_detail_view),
    path("<pk>/update", product_update_view),
    path("<pk>/delete", product_destroy_view),
]
