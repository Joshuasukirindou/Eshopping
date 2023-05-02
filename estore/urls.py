from django.urls import path
from . import views

urlpatterns = [
    path('', views.estore, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('home/', views.home, name='home')

]
