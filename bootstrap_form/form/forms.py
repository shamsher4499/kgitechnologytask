from django import forms
from django.db.models import fields
from .models import *
from django.core import validators

class VehicalForm(forms.ModelForm):
    class Meta:
        model = VehicleGeneralForm
        fields = ['vehicle_no', 'wheeler',]

# class StatusForm(forms.ModelForm):
#     class Meta:
#         model = StatutoryDetails
#         exclude = ('user',)

# class OtherForm(forms.ModelForm):
#     class Meta:
#         model = OtherDetails
#         exclude = ('user',)