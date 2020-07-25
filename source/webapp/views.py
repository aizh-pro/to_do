from django.shortcuts import render
from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': data
    })


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', context={'status_choices': STATUS_CHOICES})
    elif request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        if deadline == '':
            task = Task.objects.create(title=title, deadline=None, status=status)
        else:
            task = Task.objects.create(title=title, deadline=deadline, status=status)
        context = {
            'task': task,
        }
        return render(request, 'task_view.html', context)

