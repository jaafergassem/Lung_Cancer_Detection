from django.forms import ModelForm
from django import forms 
from .models import DetectionResult    

class DetectionResultForm(forms.ModelForm):
    class Meta:
        model = DetectionResult  
        fields = '__all__'
