from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from datetime import datetime


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    date_of_birth = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address',
                  'date_of_birth', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.address = self.cleaned_data['address']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'phone_number', 'address', 'date_of_birth')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
        }
