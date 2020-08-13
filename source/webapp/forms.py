from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from .models import STATUS_CHOICES, Status, Type, Task

default_status = STATUS_CHOICES[0][0]


BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, value, limit):
        return value < limit

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