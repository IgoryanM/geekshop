from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import ProductCategory, Product


def main(request):
    products = Product.objects.all()[:4]
    content = {
        'title': 'main',
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    basket = 0
    if request.user.is_authenticated:
        basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))

    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all().order_by('price')
            category_item = {}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category=category_item)
        content = {
            'title': 'products',
            'links_menu': links_menu,
            'category_item': category_item,
            'products': products_list,
            'basket': basket
        }
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()

    content = {
        'title': 'products',
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'contact'
    }
    return render(request, 'mainapp/contact.html', content)
