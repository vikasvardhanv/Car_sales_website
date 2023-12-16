from django import forms
from .models import CarModel

class MusicianForm(forms.ModelForm):
    class Meta:
        model = CarModel
        # fields = '__all__'
        exclude = ['brand']