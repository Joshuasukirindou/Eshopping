from django.urls import path
from . import views

urlpatterns = [
    path('', views.estore, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('home/', views.home, name='home'),
    path('add_Items/', views.addItems, name='add_Items'),
    path('access_order/', views.processOrder, name='access_order'),
    path('detail/<int:product_id>/', views.product_detail, name='detail')


]
