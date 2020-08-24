from django.core.paginator import Paginator
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


# class ProjectView(DetailView):
#     template_name = 'project/project_view.html'
#     model = Project
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project
    paginate_tasks_by = 5
    paginate_tasks_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tasks, page, is_paginated = self.paginate_tasks(self.object)
        context['tasks'] = tasks
        context['page_obj'] = page
        context['is_paginated'] = is_paginated

        return context

    def paginate_tasks(self, project):
        tasks = project.tasks.all().order_by('-created_at')
        if tasks.count() > 0:
            paginator = Paginator(tasks, self.paginate_tasks_by, orphans=self.paginate_tasks_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1
            return page.object_list, page, is_paginated
        else:
            return tasks, None, False


class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})