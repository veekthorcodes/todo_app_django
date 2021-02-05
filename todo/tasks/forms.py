from django.db.models import fields
from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Enter Task', 'class':'form-control mb-2'}
        )
    )
    class Meta:
        model = Task
        fields = '__all__'

    # def __inti__(self, *args, **kwargs):
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     for field in iter(self.fields):
    #         self.fields[field].widget.attrs.update({
    #             "class":'form-control'
    #         })
    