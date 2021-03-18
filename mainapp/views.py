from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    products = Product.objects.all()[:4]
    content = {
        'title': 'main',
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    same_products = Product.objects.all()
    links_menu = ProductCategory.objects.all()
    content = {
        'title': 'products',
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'contact'
    }
    return render(request, 'mainapp/contact.html', content)
