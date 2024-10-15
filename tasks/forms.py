from django.forms import ModelForm
from django.forms.widgets import Input
from tasks.models import Task

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']
        widgets = {
            "name": Input(attrs={
                'id': 'taskTitle',
                'class': 'form-control',
                'type': 'text',
                'name': 'taskTitle',
                'placeholder': 'Title',
            }),
            "description": Input(attrs={
                'id': 'taskDescription',
                'class': 'form-control',
                'type': 'text',
                'name': 'taskDescription',
                'placeholder': 'Description',
            })
        }
