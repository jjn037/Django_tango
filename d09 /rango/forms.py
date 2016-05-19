from django import forms
from rango.models import Students
from django.contrib.auth.models import User


class Stu_form(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Please enter your name")
    card_no = forms.IntegerField(help_text="Please enter your card number")
    sex = forms.CharField(max_length=100, help_text="Please enter your sex")
    grade = forms.CharField(max_length=100, help_text="Please enter your grade")
    picture = forms.ImageField(help_text="Please upload your profile")

    class Meta:
        model = Students
        exclude = ('slug',)


class User_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')