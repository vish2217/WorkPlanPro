from django.forms import ModelForm
   

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .models import Task
from .models import CustomerMessage

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())  
    password=forms.CharField(widget=TextInput())       

#task 

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields = ['title', 'description', 'due_date'] 
class CustomerMessageForm(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = ['name', 'email', 'message']