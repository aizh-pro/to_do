from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in progress', 'В процессе'),
    ('done', 'Сделано')
]

DEFAULT_TYPE = 'Task'
TYPE_CHOICES = [
    ('Task', 'задача'),
    ('Bug', 'ошибка'),
    ('Enhancement ', 'улучшение')
]

class Project(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=255, null=True, blank=True, verbose_name='Описание', validators=[MaxLengthValidator(255)])
    start_date = models.DateField(null=False, blank=False, verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание', validators=[MinLengthValidator(10)])
    deadline = models.DateField(null=True, blank=True, verbose_name='Дедлайн')
    description = models.TextField(max_length=255, null=True, blank=True, verbose_name='Подробное описание',validators=[MaxLengthValidator(255)])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    type = models.ManyToManyField('webapp.Type', related_name='task_type', verbose_name='Тип', blank=False)
    status = models.ForeignKey('webapp.Status', related_name='task_status', on_delete=models.PROTECT, verbose_name='Статус')
    project = models.ForeignKey('webapp.Project', related_name='tasks', on_delete=models.CASCADE, verbose_name='Проект')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='Задача')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


