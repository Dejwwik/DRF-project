from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from . import client


class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        tag = request.GET.get("tag") or None
        if not query:
            return Response(data="", status=400)
        results = client.perform_search(query, tags=tag)
        return Response(data=results, status=200)


class SearchListOldView(generics.ListAPIView):
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
