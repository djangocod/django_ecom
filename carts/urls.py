from django import views
from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('',views.cart_view,name='cart_view'),
    path('add-to-cart/',views.cart_add_product,name='add_to_cart_one'),
    path('add-to-cart-detail/', views.cart_add_product_from_detail,
         name='cart_add_product_from_detail'),
    path('update-cart-qty/',views.update_cart,name='update_cart'),
    path('delete-cart-qty/', views.delete_cart_item, name='delete_cart_item'),
    path('placeorder/', views.place_order_cart, name='place_order_cart'),
    path('checkoutcart/', views.checkout_cart, name='checkout_cart'),
 
]
