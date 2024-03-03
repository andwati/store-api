from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    barcode = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
