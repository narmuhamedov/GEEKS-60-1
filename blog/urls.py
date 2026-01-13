from django.urls import path
from . import views

urlpatterns = [
    path('blog_one/', views.first_blog, name='blog_one'),
    path('blog_two/', views.second_blog, name='blog_two'),
    path('blog_three/', views.third_blog),
    path('current_time/', views.data_time),
    path('search/', views.search_view, name='search'),
    path('', views.blog, name='home_page'),
    path('blog_list/<int:id>/', views.blog_detail),
]

