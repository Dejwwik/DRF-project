from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        if q := self.request.GET.get("q"):
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            return qs.search(q, user=user)
        return Product.objects.none()


search_list_view = SearchListView.as_view()
