from django.shortcuts import render
from django.views.generic import ListView, CreateView
from cities.models import City
from cities.forms import CityForm


__all__ = [
    'CityListView',
    'CityCreateView',
]


class CityListView(ListView):
    model = City
    template_name = 'cities/home.html'
    paginate_by = 5


class CityCreateView(CreateView):
    template_name = 'cities/add_city.html'
    form_class = CityForm
    # success_url = '/thanks/'


