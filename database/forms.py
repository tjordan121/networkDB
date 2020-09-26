from django import forms
from .models import Device

class deviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['hostname', 'IPAddress', 'deviceType', 'family', 'model']