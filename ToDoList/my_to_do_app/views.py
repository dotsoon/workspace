from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from.models import*

from django.urls import reverse

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render( request, 'my_to_do_app/index.html', content)

def createTodo( request ):
  user_input_str = request.POST['todoContent']

  new_todo = Todo(content=user_input_str)
  new_todo.save()

  return HttpResponseRedirect(reverse('index'))

def deleteTodo( request ):

  todo = Todo.objects.get(id=request.GET['todoNum'])
  todo.delete()

  return HttpResponseRedirect(reverse('index'))