from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from .models import Voter


class VoterForm(forms.ModelForm):
    pincode = forms.CharField(max_length=6, min_length=6, required=True)

    class Meta:
        model = Voter
        fields = '__all__'

        widgets = {
            'voter_id': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                                   attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pincode', 'pattern': '[0-9]{6}'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number', 'pattern': '[0-9]{10}'}),
        }

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        contact = str(contact)
        if len(contact) != 10 or not contact.isdigit():
            raise ValidationError('Contact must be exactly 10 digits.')
        return contact

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if (date.today().year - dob.year) < 18:
            raise ValidationError('Age must be 18 or above.')
        return dob

    def clean_pincode(self):
        pincode = self.cleaned_data.get('pincode')
        if not pincode.isdigit():
            raise ValidationError('Pincode must contain only digits.')
        return pincode
