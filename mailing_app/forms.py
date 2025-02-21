from django import forms
from mailing_app.models import Mailing
from django.forms import BooleanField


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field, in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['next_mailing', 'frequency', 'clients', 'mail']
        widgets = {
            'next_mailing': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'frequency': forms.Select(attrs={'class': 'form-control'}),
            'clients': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'mail': forms.Select(attrs={'class': 'form-control'}),
        }
