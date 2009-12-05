from django import forms
from django.forms.widgets import Textarea

class ViewerForm(forms.Form):
    description = forms.CharField(widget=Textarea(attrs={'cols': 90, 'rows': 15}), required=False)