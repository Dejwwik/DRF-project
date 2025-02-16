from rest_framework import generics, status, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermissions

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def perform_create(self, serializer: ProductSerializer):
        content = serializer.validated_data.get("content")
        if not content:
            content = serializer.validated_data["title"]
        serializer.save(content=content)


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailApiView.as_view()
product_create_list_view = ProductListCreateApiView.as_view()
product_update_view = ProductUpdateApiView.as_view()
product_destroy_view = ProductDestroyApiView.as_view()

# FUNCTION BASED API VIEW -> NOT PRACTICAL, TOO MUCH WORK, BUT BETTER CONTROL
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        # Detail get method /products/<pk>
        if pk is not None:
            instance = get_object_or_404(Product, pk=pk)
            return Response(
                data=ProductSerializer(instance).data,
                status=status.HTTP_200_OK
            )

        # List get method /products/
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(
            data = data,
            status = status.HTTP_200_OK
        )

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        content = serializer.validated_data.get("content")
        if not content:
            content = serializer.validated_data["title"]
        serializer.save(content=content)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
