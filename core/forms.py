from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Assignment

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'industry', 'duration', 'rate', 'requirements', 'description']
        
    def clean_description(self):
        description = self.cleaned_data.get('description')
        # Check if description contains contact details (basic check)
        contact_keywords = ['email', '@', 'phone', 'contact', 'call', 'whatsapp', 'telegram']
        
        if any(keyword in description.lower() for keyword in contact_keywords):
            raise forms.ValidationError('Description cannot contain contact information')
        return description