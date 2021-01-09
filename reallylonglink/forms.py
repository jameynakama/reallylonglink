from django import forms

from reallylonglink import models


class ReallyLongLinkForm(forms.ModelForm):
    # TODO & TOTEST: URL validation
    class Meta:
        model = models.ReallyLongLink
        fields = ["original_link"]
