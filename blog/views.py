from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog

#Получение данных
def blog(request):
    if request.method == "GET":
        #query - запрос из Базы данных указывает под видом переменной blog
        blog = Blog.objects.all()
        #Указываем где будем возвращать 
    return render(
        #в нашем запросе
        request,
        #в каком html шаблоне
        template_name='blog/blog_list.html',
        # blog который в кавычках это ключ который будет передан 
        #на html шаблон - и затем будет вывод данных
        context={
            'blog': blog
        } 
    )

#BLog detail
def blog_detail(request, id):
    if request.method == "GET":
        blog_id = get_object_or_404(Blog, id=id)
    return render(
        request, 
        template_name='blog/blog_detail.html',
        context={
            'blog_id': blog_id
        }
    )






def first_blog(request):
    if request.method == 'GET':
        return HttpResponse("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    
def second_blog(request):
    if request.method == 'GET':
        return HttpResponse("Привет меня зовут Радомир я FullStack Developer")
    
def third_blog(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9RaqWhNrT68sVwQFo4ZAs1VRsUZImppmaqg&s">  ')
    