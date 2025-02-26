from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'stock_count', 'status', 'price', 'updated_at')
    search_fields = ('name',)
    list_filter = ('status',)

