from django import forms
from .models import AssistanceRequest

class AssistanceRequestForm(forms.ModelForm):
    class Meta:
        model = AssistanceRequest
        fields = ['location', 'vehicle_type', 'description']