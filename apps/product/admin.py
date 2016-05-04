from django.contrib import admin

# Register your models here.
from apps.product.models import Product, ProductFeature, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'frontal_image', 'back_image', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ['title', 'is_active']


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'is_active',)
    list_filter = ('is_active', 'product')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active',)
    list_filter = ('is_active',)