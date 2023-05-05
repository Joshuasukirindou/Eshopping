from django.urls import path
from . import views
from .views import user_list

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('user/', views.user_list, name='userlist'),
    path('adduser/', views.add_user, name='add_user'),
    path('remove/<int:user_id>/', views.remove_user, name='remove_user')
]