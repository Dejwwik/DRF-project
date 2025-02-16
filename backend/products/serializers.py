from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validations import validate_title


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Product
        fields = (
            "id",
            "edit_url",
            "url",
            "content",
            "title",
            "price",
            "sale_price",
            "discount",
        )

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):
        return obj.get_discount()
