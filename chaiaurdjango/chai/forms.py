from django import forms
from .models import chaiVariety

class chaiVariteyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=chaiVariety.objects.all(), label="Select chai Variety")