from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'location', 'status']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters long.")
        return description