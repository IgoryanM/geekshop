from django.urls import path

import orderapp.views as orderapp

app_name = 'orderapp'

urlpatterns = [
    path('', orderapp.OrderListView.as_view(), name='order_list'),
    path('create/', orderapp.OrderCreateView.as_view(), name='order_create'),
    path('read/<int:pk>/', orderapp.OrderDetailView.as_view(), name='order_read'),
    path('update/<int:pk>/', orderapp.OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>/', orderapp.OrderDeleteView.as_view(), name='order_delete'),

    path('product/<int:pk>/price/', orderapp.get_product_price),
    path('forming/complete/<int:pk>/', orderapp.order_forming_complete, name='order_forming_complete'),
]
