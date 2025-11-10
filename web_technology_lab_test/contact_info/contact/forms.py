from django import forms
from .models import ContactInfo

class Contactform(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['name', 'email', 'phonenumber', 'address']