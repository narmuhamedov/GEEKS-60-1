from django.urls import path
from . import views

urlpatterns = [
    path('blog_one/', views.first_blog, name='blog_one'),
    path('blog_two/', views.second_blog, name='blog_two'),
    path('blog_three/', views.third_blog),
    path('current_time/', views.data_time),
    path('search/', views.SearchView.as_view(), name='search'),
    path('', views.BlogListView.as_view(), name='home_page'),
    path('blog_list/<int:id>/', views.BlogDetailView.as_view()),
]

