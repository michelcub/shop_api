from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=10
    )
    img = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name="categories")

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product {self.name} - price {self.price}"


class Stock(models.Model):
    product = models.ForeignKey(Product, related_name="stock", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"
