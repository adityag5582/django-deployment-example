from django import forms
from django.core import validators



class userform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_mail = forms.EmailField(label="enter your mail again: ")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        Email = all_clean_data['email']
        vmail = all_clean_data['verify_mail']
        if Email != vmail:
            raise forms.ValidationError("please enter same mail")
