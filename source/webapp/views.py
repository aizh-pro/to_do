from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from webapp.models import Task
from .forms import TaskForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)

        context['task'] = task
        return context

class TaskCreateView(FormView):
    template_name = 'task_create.html'
    form_class = TaskForm

    def form_valid(self, form):
        data = {}
        for key, value in form.cleaned_data.items():
            if value is not None:
                data[key] = value
        self.task = Task.objects.create(**data)
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})


class TaskUpdateView(FormView):
    template_name = 'task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_initial(self):
        initial = {}
        for key in 'title', 'description', 'deadline', 'status', 'type':
            initial[key] = getattr(self.task, key)
        return initial

    def form_valid(self, form):
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.task, key, value)
        self.task.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                if value is not None:
                    setattr(task, key, value)
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return self.render_to_response({
                'article': task,
                'form': form
            })


class TaskDeleteView(TemplateView):
    template_name = 'task_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
        return context

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')




