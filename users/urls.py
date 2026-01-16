from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('user_list/', views.user_list_view, name='user_list'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout')
]