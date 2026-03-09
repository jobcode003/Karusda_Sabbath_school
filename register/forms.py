from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'second_name', 'phone_number', 'year_of_study', 'class_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'placeholder': 'Second Name', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
            'year_of_study': forms.Select(attrs={'class': 'form-control'}),
            'class_name': forms.Select(attrs={'class': 'form-control'}),
        }
