from django import forms
from .models import *

# class MailForm(forms.ModelForm):
#
#     # class Meta:
#         # model = Mail
#         exclude = [""]


class MailForm(forms.Form):
    def __init__(self, choices, *args, **kwargs):
        super(MailForm, self).__init__(*args, **kwargs)
        self.fields['product'].choices = choices
    product = forms.ChoiceField(required=True)
    email = forms.EmailField()
    name = forms.CharField(max_length=128)
    phone = forms.CharField(max_length=12)
    message = forms.Textarea()