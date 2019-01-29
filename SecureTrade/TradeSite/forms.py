from django import forms

class RegistForm(forms.Form):
    post = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'input'}))