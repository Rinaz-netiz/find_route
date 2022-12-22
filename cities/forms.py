from django import forms
from cities.models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(label='Город', max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Введите имя города'}))

    class Meta:
        model = City
        fields = ('name', )
