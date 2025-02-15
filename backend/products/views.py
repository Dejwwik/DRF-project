from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer: ProductSerializer):
        content = serializer.validated_data.get("content")
        if not content:
            content = serializer.validated_data["title"]
        serializer.save(content=content)

product_detail_view = ProductDetailApiView.as_view()
product_create_view = ProductCreateApiView.as_view()