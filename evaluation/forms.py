from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.db import models
from .models import FeedbackDetails,Trainer,Course
from django.contrib.auth.forms import UserCreationForm

class MyModel(forms.ModelForm):
        class Meta:
            model = FeedbackDetails
            fields ="__all__"
            objects = models.Manager()

           
class RegularUserSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

      
    


class AdminSignupForm(UserCreationForm):
    organization = forms.CharField(max_length=100, required=True)
    

