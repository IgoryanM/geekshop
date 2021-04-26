from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='media_for_users')
def media_for_users(path_to_avatar):
    if not path_to_avatar:
        path_to_avatar = 'users_avatars/default.jpg'

    return f'{settings.MEDIA_URL}{path_to_avatar}'


def media_for_products(path_to_img):
    if not path_to_img:
        path_to_img = 'product_images/default.jpg'

    return f'{settings.MEDIA_URL}{path_to_img}'


register.filter('media_for_products', media_for_products)
