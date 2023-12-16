from django import forms 
from .models import BrandModel

class BrandForm(forms.ModelForm):
    class Meta:
        moodel = BrandModel
        fields = '__all__'