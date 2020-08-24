
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.datetime_safe import date
from django.utils.deconstruct import deconstructible
from .models import STATUS_CHOICES, Task, Project

default_status = STATUS_CHOICES[0][0]


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, value, limit):
        return value < limit

    def clean(self, value):
        return len(value)


@deconstructible
class MaxLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be max %(limit_value)d symbols long!'
    code = 'too_long'

    def compare(self, value, limit):
        return value > limit

    def clean(self, value):
        return len(value)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description', 'status','type', 'deadline']
        widgets = {'type': forms.CheckboxSelectMultiple}


    def clean(self):
        cleaned_data = super().clean()
        errors = []
        description = cleaned_data.get('description')
        title = cleaned_data.get('title')
        status = cleaned_data.get('status')
        if description and title and description == title:
            errors.append(ValidationError("Text of the article should not duplicate it's title!"))
        if title and status and title == description:
            errors.append(ValidationError("It's a spam!"))
        if errors:
            raise ValidationError(errors)
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Title is too long!')
        return title

    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
        if date.today() >= deadline:
            raise ValidationError("The date cannot be in the past!")
        return deadline


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description','start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        errors = []
        description = cleaned_data.get('description')
        name = cleaned_data.get('name')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if description and name and description == name:
            errors.append(ValidationError("Text  should not duplicate it's name!"))
        if errors:
            raise ValidationError(errors)
        return cleaned_data