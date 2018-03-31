from django.shortcuts import render
from lists.models import *
from collections import Counter

# Create your views here.


def ships(request):
    ships = Ship.objects.all()
    context_dict = {'ships': ships}
    return render(request, 'lists.html', context_dict)


def index(request):
    return render(request, 'main.html')


def crushers(request):
    ships_filtered = Ship.objects.filter(side="Империя", type="Звездный разрушитель")
    context_dict = {'ships': ships_filtered}
    return render(request, 'crushers.html', context_dict)


def long(request):
    long_ships = Ship.objects.filter(lenght__gt=1000).order_by('-lenght')
    context_dict = {'ships': long_ships}
    return render(request, 'long.html', context_dict)


def count(request):

    context_dict = {'types': types}
    return render(request, 'counted.html', context_dict)
    pass

