from django import forms
from .models import Todo

class LoginForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'



