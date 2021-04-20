from django.urls import path
from adminapp import views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    #path('users/read/', adminapp.users, name='user_read'),
    path('users/read/', adminapp.UserList.as_view(), name='user_read'),
    path('users/read/<int:page>', adminapp.UserList.as_view(), name='users_page'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    #path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/create/', adminapp.ProductCategoryCreate.as_view(), name='category_create'),
    #path('categories/read/', adminapp.categories, name='category_read'),
    path('categories/read/', adminapp.ProductCategoryList.as_view(), name='category_read'),
    path('categories/read/<int:page>/', adminapp.ProductCategoryList.as_view(), name='categories_page'),

    #path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdate.as_view(), name='category_update'),
    #path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDelete.as_view(), name='category_delete'),

    path('products/create/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminapp.ProductList.as_view(), name='products'),
    #path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('products/read/<int:pk>/', adminapp.ProductDetail.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),

]
