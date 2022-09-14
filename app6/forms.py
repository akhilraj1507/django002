from django import forms
from . models import*

class carForm(forms.ModelForm):
    class Meta:
        model=cardata
        fields="__all__"

class car1(forms.ModelForm):
    class Meta:
        model=cardata
        fields=['name','dis']

class car2(forms.ModelForm):
    class Meta:
        model=cardata
        fields=['image']

    
