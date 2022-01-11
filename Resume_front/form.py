from django import forms
from .models import msgreq

class contactf(forms.ModelForm):
    class Meta:
        model = msgreq
        fields = '__all__'