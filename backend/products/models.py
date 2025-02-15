from django.db import models

class Product(models.Model):
    title = models.TextField(max_length=120)
    content = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=5)

