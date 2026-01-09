from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.forms import CustomRegisterForm
from users.models import CustomUser

#REGISTER

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = CustomRegisterForm()
    return render(
        request,
        template_name='users/register.html',
        context={'form': form}
    )

#Авторизация
def auth_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/user_list/')
    else:
        form = AuthenticationForm()
    
    return render(
        request,
        template_name='users/login.html',
        context={'form': form}
    )


#выход из аккаунта
def auth_logout_view(request):
    logout(request)
    return redirect('/login/')


def user_list_view(request):
    if request.method == 'GET':
        user_list = CustomUser.objects.all()
    return render(
        request,
        template_name='users/user_list.html',
        context={'user_list': user_list}
    )