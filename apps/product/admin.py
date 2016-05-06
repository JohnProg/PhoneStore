from django.contrib import admin

# Register your models here.
from apps.product.models import Product, ProductFeature, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'imagen', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ['title', 'is_active']

    def imagen(self, product):
        tag = '<a href="{0}"><img src="{0}" width=50px height=50px/></a>'.format(product.thumbnail)
        return tag

    imagen.allow_tags = True


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'is_active',)
    list_filter = ('is_active', 'product')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active',)
    list_filter = ('is_active',)