from django.urls import path
from cities.views import *

urlpatterns = [
    path('', CityListView.as_view(), name="home"),
    path('create/', CityCreateView.as_view(), name="create")
]
