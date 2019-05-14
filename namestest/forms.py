from django import forms
from django.forms import formset_factory

class name_form(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name'
        })
    )
name_formset = formset_factory(name_form)

