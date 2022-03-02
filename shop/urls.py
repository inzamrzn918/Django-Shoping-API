from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('products', get_products),
    path('products/<str:p_id>', get_single_product),
    path('products/tag/<str:tag_title>', get_products),
    path('products/cat/<str:cat_title>', get_products),
    path('product/new', set_products),
    path('product/update/<str:p_id>', update_products),

    path('cats', get_category),
    path('cats/<str:cat_id>', get_category_one),
    path('cat/new', set_category),
    path('cat/update/<str:cat_id>', update_category),

    path('tags', get_tag),
    path('tags/<str:tag_id>', get_tag_one),
    path('tag/new', set_tag),
    path('tag/update/<str:tag_id>', update_tag),

    path('orders/', get_orders),
    path('orders/cust/<str:customer_id>', get_single_orders),
    path('orders/od/<str:order_id>', get_single_orders),
    path('order/new', set_orders),

    #     TODO : Customer routes
    # path('customers/)

    path('register', register)
]
