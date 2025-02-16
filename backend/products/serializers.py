from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ("id", "url", "content", "title", "price", "sale_price", "discount")

    def get_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):
        return obj.get_discount()
