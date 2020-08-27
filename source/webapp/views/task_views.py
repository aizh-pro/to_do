from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.forms import SimpleSearchForm, TaskForm, ProjectTaskForm
from webapp.models import Task, Project
from django.db.models import Q


class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_context_data(self,*, object_list=None, **kwargs):
        form = SimpleSearchForm(data=self.request.GET)
        kwargs['search_form'] = form
        return super().get_context_data(object_list=object_list,**kwargs)

    def get_queryset(self):
        data = Task.objects.all()

        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(title__icontains=search) | Q(description__icontains=search))

        return data.order_by('-created_at')


class TaskView(DetailView):
    template_name = 'task/task_view.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProjectTaskCreateView(CreateView):
    model = Task
    template_name = 'task/task_create.html'
    form_class = ProjectTaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('project_view', pk=project.pk)


class TaskCreateView(CreateView):
    template_name = 'task/task_create.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/task_update.html'
    form_class = ProjectTaskForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})

# class TaskUpdateView(FormView):
#     template_name = 'task/task_update.html'
#     form_class = TaskForm
#
#     def dispatch(self, request, *args, **kwargs):
#         self.task = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['task'] = self.task
#         return context
#
#     def get_initial(self):
#         initial = {}
#         for key in 'title', 'description', 'deadline', 'status', 'type':
#             initial[key] = getattr(self.task, key)
#         initial['type'] = self.task.type.all()
#         return initial
#
#     def form_valid(self, form):
#         type = form.cleaned_data.pop('type')
#         for key, value in form.cleaned_data.items():
#             if value is not None:
#                 setattr(self.task, key, value)
#         self.task.save()
#         self.task.type.set(type)
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('task_view', kwargs={'pk': self.task.pk})
#
#     def get_object(self):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(Task, pk=pk)


# class TaskDeleteView(TemplateView):
#     template_name = 'task/task_delete.html'
# 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
# 
#         pk = self.kwargs.get('pk')
#         task = get_object_or_404(Task, pk=pk)
#         context['task'] = task
#         return context
# 
#     def post(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         task.delete()
#         return redirect('index')


class TaskDeleteView(DeleteView):
    model = Task

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})




