from django import forms 
from .models import chai_variety

class Chai_Variety_form(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=chai_variety.objects.all, label="select chai variety")