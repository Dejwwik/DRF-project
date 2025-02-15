from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product


@api_view(http_method_names=["get"])
def home(request, *args, **kwargs):
    product = Product.objects.all().order_by("?").first()
    return Response(data=model_to_dict(product), status=status.HTTP_200_OK)