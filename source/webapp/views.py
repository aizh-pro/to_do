from django.shortcuts import render

def index_view(request):
    print(request.GET.getlist('author'))
    return render(request, 'index.html')


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

