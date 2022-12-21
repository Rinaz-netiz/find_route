from django.shortcuts import render


def index(request):
    """Стартовая страница"""
    return render(request, 'base.html', {"title_page": 'HOME PAGE'})
