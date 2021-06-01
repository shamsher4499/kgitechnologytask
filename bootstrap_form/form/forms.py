from django import forms
from .models import *

class VehicalForm(forms.ModelForm):
    class Meta:
        model = VehicleGeneralForm
        exclude = ('user',)

# class StatusForm(forms.ModelForm):
#     class Meta:
#         model = StatutoryDetails
#         exclude = ('user',)

# class OtherForm(forms.ModelForm):
#     class Meta:
#         model = OtherDetails
#         exclude = ('user',)