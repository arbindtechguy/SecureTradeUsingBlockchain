from django import forms

class RegistForm(forms.Form):
    post = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'input'}))


class LoginForm(forms.Form):
    key = forms.CharField(label=" Enter Private Key ",widget=forms.PasswordInput(attrs={'class':'input'}))
    password = forms.CharField(label="Enter Password",widget=forms.PasswordInput(attrs={'class':'input'}))