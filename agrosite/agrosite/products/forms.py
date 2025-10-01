from django import forms

class ProductSearchForm(forms.Form):
    search = forms.CharField(required=False, label="Search by name")

class AdminCreationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    secret_key = forms.CharField(widget=forms.PasswordInput)