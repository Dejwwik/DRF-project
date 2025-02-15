from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET"])
def home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    return Response(data=ProductSerializer(instance).data, status=status.HTTP_200_OK)