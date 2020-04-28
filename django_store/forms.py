from django import forms
#from django.contrib.auth.models import User

from apps.users.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                max_length=50, min_length=4,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id' : 'username',
                                    'placeholder' : 'Username'
                                }))
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={
                                'class': 'form-control',
                                'id' : 'email',
                                'placeholder' : 'email@example.com'
                            }))
    password = forms.CharField(required=True,
                            widget=forms.PasswordInput(attrs={
                                'class': 'form-control',
                                'id' : 'password',
                                'placeholder' : 'Password'
                            }))
    password_repeated = forms.CharField(required=True, label='Confirm Password',
                            widget=forms.PasswordInput(attrs={
                                'class': 'form-control',
                                'id' : 'password',
                                'placeholder' : 'Password'
                            }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya existe')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya existe')
        return email
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password') != cleaned_data.get('password_repeated'):
            self.add_error('password_repeated','Password no coincide')
    
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )