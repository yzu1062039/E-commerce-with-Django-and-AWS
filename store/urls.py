from django.urls import path
from . import views

app_name = 'store'  # URL namespace for the store app

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Product listing pages
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:category_slug>/',
         views.product_list, name='product_list_by_category'),

    # Product detail page
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    # Shopping cart URLs
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/',
         views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/',
         views.remove_from_cart, name='remove_from_cart'),

    # Checkout and order URLs
    path('checkout/', views.checkout, name='checkout'),
    path('order/confirmation/<int:order_id>/',
         views.order_confirmation, name='order_confirmation'),
    path('orders/', views.order_history, name='order_history'),

    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
