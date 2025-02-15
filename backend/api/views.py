from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product


def home(request, *args, **kwargs):
    product = Product.objects.all().order_by("?").first()
    return JsonResponse(data=model_to_dict(product, ))