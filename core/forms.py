from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext as _

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
class UserProfileForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label=_("Current password"))
    new_password = forms.CharField(widget=forms.PasswordInput, label=_("New password"))
    confirm_new_password = forms.CharField(widget=forms.PasswordInput, label=_("Confirm new password"))

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists() and username!= self.instance.username:
            raise forms.ValidationError('Username already taken')
        return username



class UpdateProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Current Password', required=False)
    new_password = forms.CharField(widget=forms.PasswordInput, label='New Password', required=False)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput, label='Confirm New Password', required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')