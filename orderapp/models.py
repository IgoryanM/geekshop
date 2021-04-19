from django.conf import settings
from django.db import models

from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    READY = 'RDY'
    CANCEL = 'CNL'

    ORDER_STATUSES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'обрабатывается'),
        (PROCEEDED, 'обработан'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.TimeField(auto_now_add=True, verbose_name='создан')
    updated = models.TimeField(auto_now=True, verbose_name='изменен')
    status = models.CharField(choices=ORDER_STATUSES, default=FORMING, verbose_name='статус', max_length=3)
    is_active = models.BooleanField(default=True, verbose_name='активен')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Текущий заказ: {self.pk}'

    def total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.get_product_cost(), items)))

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()
        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='количество')

    def get_product_cost(self):
        return self.quantity * self.product.price

    @staticmethod
    def get_item(pk):
        return Order.objects.get(pk=pk)
