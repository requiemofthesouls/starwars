from django.shortcuts import render
from lists.models import *
from django.db.models import Prefetch

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
    types = Type.objects.filter(
        ship__side='Империя'
    ).prefetch_related(
        Prefetch('ship_set', queryset=Ship.objects.filter(side='Империя'))
    ).distinct()
    t = []
    c = []
    for type in types:
        qs = type.ship_set.all()
        t.append(type.type)
        c.append(len(qs))

    context_dict = {'types': t, 'counted': c}
    #  Придумать как извлечь эти данные в шаблон
    return render(request, 'counted.html', context_dict)


