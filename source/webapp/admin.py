from django.contrib import admin
from webapp.models import Task, Type, Status, Project


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'deadline', 'created_at']
    list_filter = ['status']
    search_fields = ['title', 'status']
    fields = ['title', 'status', 'deadline', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)

