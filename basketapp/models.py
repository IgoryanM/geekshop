from django.conf import settings
from django.db import models
from django.utils.functional import cached_property

from mainapp.models import Product
from orderapp.models import OrderItem


# class BasketQuerySet(models.QuerySet):
#     def delete(self):
#         for item in self:
#             item.product.quantity += item.quantity
#             item.product.save()
#         super().delete()


class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='время')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='количество')

    # @cached_property
    # def get_items_cached(self):
    #     return self.user.basket.select_related()

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
       # _items = self.get_items_cached
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        #_items = self.get_items_cached
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete()

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category')

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)
