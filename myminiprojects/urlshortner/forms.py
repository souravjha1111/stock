from django import forms

from .validators import validate_url

class SubmitForm(forms.Form):
    shortcode = forms.CharField()
    url = forms.CharField(widget = forms.TextInput(
        attrs = {
            "placeholder": "Enter Your Url Here",
            "class": "form-control"
        }
    )
    
                        )