from django import forms

class ExampleForm(forms.Form):
    """
    Example form with a few fields to demonstrate how to create a basic form.
    """
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
