from django.urls import path
from . import views

app_name = 'stores'
urlpatterns = [
    path('',views.store_home,name='store_home'),
    path('shopping/', views.store_shopping, name='store_shopping'),
    path('shopping/<slug:slug_cate>/', views.store_category_product,name='store_category_product'),
    path('product/<slug:pro_slug>/', views.store_product_details,name='product_detail'),
    path('product/sub/<slug:cat_slug>/',views.store_sub_menu_product, name='store_sub_menu_product'),
    path('search/', views.product_search, name='product_search')
]
