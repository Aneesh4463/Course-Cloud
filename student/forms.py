from django import forms

from django.contrib.auth.forms import UserCreationForm

from instructor.models import User


class StudentCreateForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","password1","password2","email"]


class LogInForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()