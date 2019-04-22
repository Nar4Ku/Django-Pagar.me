from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Usuário'}
        ))
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Senha'}
        ))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
 
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Este usuário não existe!')
            if not user.check_password(password):
                raise forms.ValidationError('Senha Incorreta!')
            if not user.is_active:
                raise forms.ValidationError('Este usuário não está ativo!')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nome'}
        ))
    last_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}
        ))
    email = forms.EmailField(
        required=True, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
        ))
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Senha'}
        ))
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirmar Senha'}
        ))
    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Usuário'}
        ))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password1',
        ]
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        email = self.cleaned_data.get('email')
        if password != password1:
            raise forms.ValidationError('As senhas não correspondem!')
        email_query_selector = User.objects.filter(email=email)
        if email_query_selector.exists():
            raise forms.ValidationError('Esse email já foi cadastrado!')
        username_query_selector = User.objects.filter(username=username)
        if username_query_selector.exists():
            raise forms.ValidationError('Esse usuário já foi cadastrado!')
        return super(UserRegisterForm, self).clean(*args, **kwargs)
