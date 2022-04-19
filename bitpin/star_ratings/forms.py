from __future__ import absolute_import
from django import forms
from django.conf import settings

from . import get_star_ratings_rating_model
from .models import UserRating


class CreateUserRatingForm(forms.ModelForm):
    clear = forms.BooleanField(required=False)

    class Meta:
        model = UserRating
        exclude = [
            'count',
            'average',
            'rating',
        ]

    def __init__(self, obj=None, *args, **kwargs):
        self.obj = obj
        super(CreateUserRatingForm, self).__init__(*args, **kwargs)

        if self.data.get('clear', False) and settings.STAR_RATINGS_CLEARABLE:
            self.fields['score'].required = False

    def save(self, commit=True):
        return get_star_ratings_rating_model().objects.rate(
            self.obj,
            self.cleaned_data['score'],
            user=self.cleaned_data['user'],
            clear=self.cleaned_data['clear'],
        )
