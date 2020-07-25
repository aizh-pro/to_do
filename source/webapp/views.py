from django.shortcuts import render
from webapp.models import Task


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': data
    })


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    elif request.method == 'POST':
        context = {
            'title': request.POST.get('title'),
            'status': request.POST.get('status'),
            'deadline': request.POST.get('deadline')
        }
        return render(request, 'task_view.html', context)

