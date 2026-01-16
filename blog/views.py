from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog
from datetime import datetime

from django.views import generic



#Поиск
class SearchView(generic.ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog'
    model = Blog

    def get_queryset(self):
        return self.model.objects.filter(name_blog__icontains=self.request.GET.get("s"))
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context
    
    




# def search_view(request):
#     query = request.GET.get('s', '')
#     if query:
#         blog = Blog.objects.filter(name_blog__icontains=query)
#     else:
#         blog = Blog.objects.none
#     return render(
#         request,
#         template_name='blog/blog_list.html',
#         context={
#             'blog': blog
#         } 
#     )






#Получение данных

class BlogListView(generic.ListView):
    template_name = 'blog/blog_list.html'
    context_object_name =  'blog'
    model = Blog

    def get_queryset(self):
        return self.model.objects.all()




# def blog(request):
#     if request.method == "GET":
#         #query - запрос из Базы данных указывает под видом переменной blog
#         blog = Blog.objects.all()
#         #Указываем где будем возвращать 
#     return render(
#         #в нашем запросе
#         request,
#         #в каком html шаблоне
#         template_name='blog/blog_list.html',
#         # blog который в кавычках это ключ который будет передан 
#         #на html шаблон - и затем будет вывод данных
#         context={
#             'blog': blog
#         } 
#     )

#BLog detail
class BlogDetailView(generic.DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog
    context_object_name = 'blog_id'

    def get_object(self, **kwargs):
        blog_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=blog_id)


# def blog_detail(request, id):
#     if request.method == "GET":
#         blog_id = get_object_or_404(Blog, id=id)
#     return render(
#         request, 
#         template_name='blog/blog_detail.html',
#         context={
#             'blog_id': blog_id
#         }
#     )





# current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def data_time(request):
    if request.method == "GET":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f'Текущее время-{current_time}')



def first_blog(request):
    if request.method == 'GET':
        return HttpResponse("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    
def second_blog(request):
    if request.method == 'GET':
        return HttpResponse("Привет меня зовут Радомир я FullStack Developer")
    
def third_blog(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9RaqWhNrT68sVwQFo4ZAs1VRsUZImppmaqg&s">  ')
    