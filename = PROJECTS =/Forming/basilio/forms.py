from django import forms
from django.core import validators

def check_for_z(value):
    if value.lower().endswith('ok'):
        raise forms.ValidationError("Please do not end your message with 'ok'")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again: ')
    text = forms.CharField(widget=forms.Textarea, validators=[check_for_z])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email addresses do not match!")
            
    # botcatcher = forms.CharField(
    #     required=False,
    #     widget=forms.HiddenInput,
    #     validators=[validators.MaxLengthValidator(0)]
    # )