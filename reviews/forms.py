from django import forms
from .models import Review


class Add_ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = (
            'rating',
            'review_text',
        )
