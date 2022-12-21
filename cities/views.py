from django.shortcuts import render
from django.views.generic import ListView
from cities.models import City


__all__ = [
    'CityView',
]


class CityView(ListView):
    model = City
    template_name = 'cities/home.html'
    paginate_by = 1
