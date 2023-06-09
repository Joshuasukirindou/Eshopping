from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import uuid

from .models import Message


def get_message_obj():
    message_obj = Message.objects.order_by('-id')
    return message_obj


def index(request):
    return render(request, 'estore/store.html')


def goto_index_view(request, url):
    # Redirect to example.com
    return HttpResponseRedirect(url)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password1 != password2:
            error_message = 'Inconsistent passwords'
            return render(request, 'useradd.html', {'error_message': error_message})
        elif username == '':
            error_message = 'Username cannot be empty'
            return render(request, 'useradd.html', {'error_message': error_message})
        user = User.objects.create_user(username=username, password=password1, email=email)
        user.save()
        login(request, user)
        return redirect('create_empty_cart')
    return render(request, 'useradd.html')




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,'successful login')
            return redirect('store')
        else:
            msg = 'Invalid login credentials'
            messages.error(request, msg)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('store'))


def guest_login(request):
    # create a temporary user with a unique username and password
    username = 'guest' + str(uuid.uuid4().hex)[:8]
    password = uuid.uuid4().hex
    user = User.objects.create_user(username=username, password=password)
    user.save()

    # log the user in
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

    # redirect to the store page
    return redirect('store')









