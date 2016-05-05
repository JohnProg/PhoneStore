from django.views.generic import TemplateView, ListView, DetailView

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.product.models import Product, Brand
from .serializers import ProductSerializer


class IndexPage(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "admin/dashboard.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        return queryset


class ProductListPage(ListView):
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

    def get_template_names(self):
        if not self.request.user.is_authenticated():
            self.template_name = 'public/login.html'
        return [self.template_name]


class BrandListPage(ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = "admin/brand_list.html"

    def get_queryset(self):
        queryset = Brand.objects.filter(is_active=True)
        return queryset

    def get_template_names(self):
        if not self.request.user.is_authenticated():
            self.template_name = 'public/login.html'
        return [self.template_name]


class ProductDetailPage(TemplateView):
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

    def get_template_names(self):
        if not self.request.user.is_authenticated():
            self.template_name = 'public/login.html'
        return [self.template_name]

@api_view(['GET'])
def products(request):
    serializer = ProductSerializer(Product.objects.filter(is_active=True).order_by('title'), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product(request, id=None):
    serializer = ProductSerializer(get_object_or_404(Product, id=id))
    return Response(serializer.data)