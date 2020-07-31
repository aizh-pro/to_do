from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Заголовок')
    description = forms.CharField(max_length=3000, required=True, label="Описание",
                           widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус',
                               initial=default_status)
    deadline = forms.DateTimeField(required=False, label='Дедлайн',
                                     input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
                                                    '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
                                                    '%Y-%m-%d %H:%M:%S'],
                                     widget=forms.DateInput(attrs={'type': 'date'}))

