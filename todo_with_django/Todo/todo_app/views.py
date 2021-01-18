from django.shortcuts import render
from .models import TodoModel
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    todo_list = TodoModel.objects.all()
    context = {"todos": todo_list}
    return render(request, "todo_app/index.html", context)


def createTodo(request):
    todoContent = request.POST['content']
    new_todo = TodoModel(content=todoContent)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))


def deletTodo(request):
    id = request.GET["id"]
    delete_id = TodoModel.objects.get(id=id)
    delete_id.delete()
    return HttpResponseRedirect(reverse('index'))


def clearTodo(request):
    todo = TodoModel.objects.all()
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

    # 0. setting.py, project urls.py 수정
    #  2. todo_with_django repository에 Todo project생성
    #  2. Todo project에 my_todo_app application 생성
    #  3. HTML/CSS Javascript 수업에서 작성한 todo
    #     index.html, js/todo.js 파일을 templates로 하는 App작성
    #  4. TodoModel : id, content - makemigration, migrate
    #  5. views(Controller) 작성(index, createTodo, deleteTodo, clearTodo)
    #  6. templates(View) 수정
    #  7. application의 urls.py 작성
