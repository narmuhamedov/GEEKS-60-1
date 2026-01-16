from django.shortcuts import render, redirect, get_object_or_404
from todo.forms import TodoForm
from todo.models import Todo
from django.views import generic

#CREATE
class CreateTodoView(generic.CreateView):
    template_name = 'todo/create_todo.html'
    form_class = TodoForm
    success_url = '/todo_list/'


    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTodoView, self).form_valid(form=form)




# def create_todo_view(request):
#     if request.method == 'POST':
#         form = TodoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/todo_list/')
#     else:
#         form = TodoForm()
    
#     return render(
#         request,
#         template_name='todo/create_todo.html',
#         context={"form": form}
#     )

#READ
class ReadTodoView(generic.ListView):
    template_name = 'todo/todo_list.html'

    def get_queryset(self):
        return Todo.objects.all().order_by('-id')





# def read_todo_view(request):
#     if request.method == 'GET':
#         todo = Todo.objects.all()
#     return render(request, template_name='todo/todo_list.html',
#                   context={'todo': todo})


#UPDATE
class UpdateTodoView(generic.UpdateView):
    template_name = 'todo/update_todo.html'
    form_class = TodoForm
    success_url = '/todo_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(Todo, id=todo_id)

# def update_todo_view(request, id):
#     todo_id = get_object_or_404(Todo, id=id)
#     if request.method == 'POST':
#         form = TodoForm(request.POST, instance=todo_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/todo_list/')
#     else:
#         form = TodoForm(instance=todo_id)
#     return render(request,
#                   template_name='todo/update_todo.html',
#                   context={
#                       'form': form,
#                       'todo_id': todo_id
#                     }
#                   )
#DELETE



class DeleteTodoView(generic.DeleteView):
    template_name = 'todo/confirm_delete.html'
    success_url = '/todo_list/'


    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(Todo, id=todo_id)


# def delete_todo_view(request, id):
#     todo_id = get_object_or_404(Todo, id=id)
#     todo_id.delete()
#     return redirect('/todo_list/')