from django import forms
from .models import * 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class date(forms.DateInput):
    input_type = "date"

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=date)
    password2 = forms.CharField(widget=date)
    
    class Meta:
        model = User
        fields = [
        "username",
        "password1",
        "password2",
        
        ]
        
class NameForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = "__all__"
        exclude = ['RegisterNumber']


class Sem1form(forms.ModelForm):
    class Meta:
        model = Sem1
        fields = "__all__"
        exclude = ["id"]


class Sem2form(forms.ModelForm):
    class Meta:
        model = Sem2
        fields = "__all__"
        exclude = ["id"]


class Sem3form(forms.ModelForm):
    class Meta:
        model = Sem3
        fields = "__all__"
        exclude = ["id"]


class Sem4form(forms.ModelForm):
    class Meta:
        model = Sem4
        fields = "__all__"
        exclude = ["id"]


class Sem5form(forms.ModelForm):
    class Meta:
        model = Sem5
        fields = "__all__"
        exclude = ["id"]




class Sem6form(forms.ModelForm):
    class Meta:
        model = Sem6
        fields = "__all__"
        exclude = ["id"]



class Sem7form(forms.ModelForm):
    class Meta:
        model = Sem7
        fields = "__all__"
        exclude = ["id"]


class Sem8form(forms.ModelForm):
    class Meta:
        model = Sem8
        fields = "__all__"
        exclude = ["id"]