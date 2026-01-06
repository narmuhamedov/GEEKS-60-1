from django.shortcuts import render, redirect, get_object_or_404
from todo.forms import TodoForm
from todo.models import Todo

#CREATE
def create_todo_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/todo_list/')
    else:
        form = TodoForm()
    
    return render(
        request,
        template_name='todo/create_todo.html',
        context={"form": form}
    )

#READ
def read_todo_view(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
    return render(request, template_name='todo/todo_list.html',
                  context={'todo': todo})


#UPDATE
def update_todo_view(request, id):
    todo_id = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo_id)
        if form.is_valid():
            form.save()
            return redirect('/todo_list/')
    else:
        form = TodoForm(instance=todo_id)
    return render(request,
                  template_name='todo/update_todo.html',
                  context={
                      'form': form,
                      'todo_id': todo_id
                    }
                  )
#DELETE

def delete_todo_view(request, id):
    todo_id = get_object_or_404(Todo, id=id)
    todo_id.delete()
    return redirect('/todo_list/')