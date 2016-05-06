from django.views.generic import TemplateView, ListView, DetailView

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from braces.views import LoginRequiredMixin

from apps.product.models import Product, Brand
from apps.users.models.StoreProduct import StoreProduct
from apps.users.models.User import User
from .serializers import ProductSerializer


class IndexPage(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = "admin/dashboard.html"
    paginate_by = 10

    def get_queryset(self):
        store = User.objects.get(id=self.request.user.id).stores.first()
        stores_product = StoreProduct.objects.filter(store=store, is_visible=True)
        productList = []
        for store_product in stores_product:
            productList.append(store_product.product)
        queryset = productList
        return queryset


class ProductListPage(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = "admin/product_list.html"

    def get_queryset(self):
        brand_id = self.kwargs['brand_id']
        queryset = Product.objects.filter(is_active=True, brand_id=brand_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        brand_id = self.kwargs['brand_id']
        context.update({
            'brand': Brand.objects.get(id=brand_id)
        })
        return context


class BrandListPage(LoginRequiredMixin, ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = "admin/brand_list.html"

    def get_queryset(self):
        queryset = Brand.objects.filter(is_active=True)
        return queryset


class ProductDetailPage(LoginRequiredMixin, TemplateView):
    template_name = "admin/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailPage, self).get_context_data(**kwargs)
        brand_id = self.kwargs['brand_id']
        product_id = self.kwargs['product_id']
        context.update({
            'brand': Brand.objects.get(id=brand_id),
            'product': Product.objects.get(id=product_id, is_active=True)
        })
        return context


@api_view(['GET'])
def products(request):
    serializer = ProductSerializer(Product.objects.filter(is_active=True).order_by('title'), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product(request, id=None):
    serializer = ProductSerializer(get_object_or_404(Product, id=id))
    return Response(serializer.data)