from django import forms

class ProductSearchForm(forms.Form):
    search = forms.CharField(required=False, label="Search by name")
