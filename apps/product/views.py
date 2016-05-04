from django.views.generic import TemplateView, ListView

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.product.models import Product
from .serializers import ProductSerializer


class IndexPage(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "admin/dashboard.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        return queryset


class ProductListPage(TemplateView):
    template_name = 'public/login.html'

    def get_template_names(self):
        if self.request.user.is_authenticated():
            self.template_name = 'admin/product_list.html'
        return [self.template_name]


class BrandListPage(TemplateView):
    template_name = 'public/login.html'

    def get_template_names(self):
        if self.request.user.is_authenticated():
            self.template_name = 'admin/brand_list.html'
        return [self.template_name]


@api_view(['GET'])
def products(request):
    serializer = ProductSerializer(Product.objects.filter(is_active=True).order_by('title'), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product(request, id=None):
    serializer = ProductSerializer(get_object_or_404(Product, id=id))
    return Response(serializer.data)