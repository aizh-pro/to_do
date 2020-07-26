from django.shortcuts import render
from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': data
    })


def task_view(request):
    task_id = request.GET.get('pk')
    task = Task.objects.get(pk=task_id)
    context = {'task': task}
    return render(request, 'task_view.html', context=context)


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', context={'status_choices': STATUS_CHOICES})
    elif request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        description = request.POST.get('description')
        if deadline == '' and description == '':
            task = Task.objects.create(title=title, deadline=None, status=status, description=None)
        elif description == '':
            task = Task.objects.create(title=title, deadline=deadline, status=status, description=None)
        elif deadline == '':
            task = Task.objects.create(title=title, deadline=None, status=status, description=description)
        else:
            task = Task.objects.create(title=title, deadline=deadline, status=status, description=description)
        context = {
            'task': task,
        }
        return render(request, 'task_view.html', context)


