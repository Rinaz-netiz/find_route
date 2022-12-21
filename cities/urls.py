from django.urls import path
from cities.views import *

urlpatterns = [
    path('', CityView.as_view(), name="home")
]