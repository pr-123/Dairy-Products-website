# forms.py
from django import forms
from .models import Contact
from .models import User
from django.contrib.auth.forms import AuthenticationForm
# for hashing the Confirm_password
from django.contrib.auth.hashers import make_password, check_password
from phonenumber_field.formfields import PhoneNumberField




class ContactForm(forms.ModelForm):
    class Meta:
         
          # Phone number field
         model = Contact
         fields = ['name', 'email', 'message','phone_number']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        hashed_password=make_password('password')
        check_hashed_password=check_password('password',hashed_password)
        if check_hashed_password:
            if commit:
                user.save()
            return user
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    fields=['username','password']

