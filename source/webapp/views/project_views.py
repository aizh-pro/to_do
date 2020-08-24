from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectListView(ListView):
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_context_data(self,*, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list,**kwargs)

    def get_queryset(self):
        data = Project.objects.all()
        return data


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})