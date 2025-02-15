from .views import ProductDetailApiView
from django.urls import path

urlpatterns = [
    path("<pk>/", ProductDetailApiView.as_view(), name="product_detail")
]
