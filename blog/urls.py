from django.urls import path
from . import views

urlpatterns = [
    path('blog_one/', views.first_blog),
    path('blog_two/', views.second_blog),
    path('blog_three/', views.third_blog),
    
    path('blog_list/', views.blog),
    path('blog_list/<int:id>/', views.blog_detail),
]

