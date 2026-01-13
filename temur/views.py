from django.shortcuts import render
from temur.models import ProductTemur

def all_orders(request):
    if request.method == "GET":
        all_orders = ProductTemur.objects.all().order_by("-id")
    return render(
            request,
            template_name='temur/all_orders.html',
            context={
                'all_orders': all_orders
            }
        )

def akylai_orders(request):
      if request.method == "GET":
          all_orders = ProductTemur.objects.filter(customers__name='Акылай')
      return render(
        request,
        template_name='temur/akylai.html',
        context={
            'all_orders': all_orders
            }
        )