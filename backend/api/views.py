from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET", "POST"])
def home(request, *args, **kwargs):
    if request.method.lower() == "get":
        instance = Product.objects.all().order_by("?").first()
        return Response(
            data=ProductSerializer(instance, context={"request": request}).data,
            status=status.HTTP_200_OK,
        )
    if request.method.lower() == "post":
        serializer = ProductSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
