from django import forms
from .models import SiteReviews


class SiteReviewsForm(forms.ModelForm):
    user = forms.IntegerField(required=True, widget=forms.HiddenInput())

    class Meta:
        model = SiteReviews
        exclude = (
            'date',)
        fields = {
            'user',
            'rating',
            'review',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'user': '',
            'rating': '',
            'review': 'Tell us how our service was!',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = placeholders[field]
                self.fields[field].label = False
                self.fields[field].widget.attrs['placeholder'] = placeholder
