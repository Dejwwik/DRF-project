from rest_framework import serializers
from .models import Product
from .validations import validate_title
from api.serializers import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    title = serializers.CharField(validators=[validate_title])
    owner = UserPublicSerializer(read_only=True, source="user")

    class Meta:
        model = Product
        fields = (
            "id",
            "owner",
            "url",
            "content",
            "title",
            "price",
        )
