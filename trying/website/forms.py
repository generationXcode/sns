from django import forms
from .models import Roast
from django.utils import timezone
class RoastForm(forms.Form):
    roast = forms.CharField(label='roast', max_length=1000)