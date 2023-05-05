from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('adduser/', views.register, name='add_user'),
    path('admin/login/', auth_view.LoginView.as_view(), name='login'),
    path('admin/logout/', auth_view.LogoutView.as_view(), name='logout'),

]