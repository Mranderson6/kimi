from django import forms
from .models import * 

class bodyAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': 'richtext_field'}))

    class Meta:
        model = BlogPost
        fields = "__all__"