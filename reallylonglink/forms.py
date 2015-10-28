from django import forms

from reallylonglink.models import ReallyLongLink


class ReallyLongLinkForm(forms.ModelForm):
    # TODO & TOTEST: URL validation
    class Meta:
        model = ReallyLongLink
        fields = ['original_link']