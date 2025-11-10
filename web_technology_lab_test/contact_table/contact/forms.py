from django import forms
from .models import contactinfo

class contactinfoform(forms.ModelForm):
    class Meta:
        model=contactinfo
        fields=['name', 'email', 'mobile', 'address']