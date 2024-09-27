from django import forms
from .models import UserProfile, Appointment

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time']
