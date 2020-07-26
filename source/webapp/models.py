from django.db import models

STATUS_CHOICES = [
    ('new','Новая'),
    ('in progress','В процессе'),
    ('done','Сделано')
]

class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new', verbose_name='Новая')
    deadline = models.DateField(null=True, blank=True, verbose_name='Дедлайн')
    description = models.TextField(max_length=255,null=True, blank=True, verbose_name='Подробное описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
