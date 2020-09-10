from django.urls import path

from webapp.views import IndexView, TaskView, TaskUpdateView, TaskDeleteView, ProjectListView, \
    ProjectView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectTaskCreateView, ProjectUserView

app_name = 'webapp'

urlpatterns = [
    path('tasks', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/add/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/tasks/add', ProjectTaskCreateView.as_view(), name='task_create'),
    path('project/<int:pk>/user/', ProjectUserView.as_view(), name='project_user'),
]