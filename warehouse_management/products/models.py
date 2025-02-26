from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Unique product ID
    name = models.CharField(max_length=255, unique=True)
    stock_count = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=50, choices=[('Available', 'Available'), ('Out of Stock', 'Out of Stock')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
