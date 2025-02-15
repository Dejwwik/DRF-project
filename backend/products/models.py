from django.db import models

class Product(models.Model):
    title = models.TextField(max_length=120)
    content = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=5)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self) -> float:
        return int(self.price) * 0.1
