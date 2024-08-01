from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
path('', views.cart_summary, name="cart_summary"),

path('add/', views.cart_add, name="cart_add"),
path('delete/', views.cart_delete, name="cart_delete"),
path('update/', views.cart_update, name="cart_update"),
path('checkout/', views.checkout, name='checkout'),
path('payment/<int:order_id>/', views.payment, name='payment'),
path('payment_success/', views.payment_success, name='payment_success'),


]
