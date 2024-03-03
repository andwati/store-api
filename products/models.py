from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    supplier = models.ForeignKey(Supplier, models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}"
