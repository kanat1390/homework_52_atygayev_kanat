from secrets import choice
from telnetlib import STATUS
from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['description', 'status', 'date']
