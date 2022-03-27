from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop_page, name='shop'),
    path(
        'product/<product_id>', views.product_details, name='product-details'
    ),
    path('wishlist/', views.wishlist, name='wishlist'),
]
