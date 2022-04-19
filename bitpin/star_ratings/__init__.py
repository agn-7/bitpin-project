from __future__ import unicode_literals

import swapper

from django.conf import settings


def get_star_ratings_rating_model_name():
    return swapper.get_model_name('star_ratings', 'Rating')


def get_star_ratings_rating_model():
    return swapper.load_model('star_ratings', 'Rating')