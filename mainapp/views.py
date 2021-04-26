from django.shortcuts import render
from

def main(request):
    title = 'главная'
    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:3]

    content = {
        'title': title,
        'products': products,
    }

    return render(request, 'mainapp/index.html', content)


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'title': 'products',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'contact'
    }
    return render(request, 'mainapp/contact.html', content)
