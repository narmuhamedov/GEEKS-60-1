from django.urls import path
from . import views


urlpatterns = [
    path('all_orders/', views.all_orders, name='all_ord'),
    path('akylai_order/', views.akylai_orders, name='akylai'),
]   