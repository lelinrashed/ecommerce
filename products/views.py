from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

from products.models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    template_name = "products/list.html"
    return render(request, template_name, context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context


def product_detail_view(request, id):
    # instance = Product.objects.get(id=id)
    instance = get_object_or_404(Product, id=id)
    context = {
        "object": instance
    }
    template_name = "products/detail.html"
    return render(request, template_name, context)


