from django import forms
from .models import Plate


class PlateForm(forms.ModelForm):

    class Meta:
        model = Plate
        fields = ('plateNumber', 'street', 'zipCode', 'city')
