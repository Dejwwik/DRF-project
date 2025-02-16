from django.db import models
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user:
            qs = (self.filter(user=user).filter(lookup) | qs).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self) -> ProductQuerySet:
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user)


class Product(models.Model):
    title = models.TextField(max_length=120)
    content = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=5)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="products"
    )
    public = models.BooleanField(default=True)

    objects = ProductManager()

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self) -> float:
        return int(self.price) * 0.1
