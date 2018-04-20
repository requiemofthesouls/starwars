from django.shortcuts import render, redirect
from lists.forms import *
from django.http import HttpResponse
from django.db.models import Prefetch
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def log_out(request):
    logout(request)
    return redirect('/')


def log_in(request):
    context_dict = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('Your account is disabled.')
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse('Invalid login details supplied.')
    else:
        return render(request, 'log_in.html', context_dict)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect('/')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'register.html', {'user_form': user_form,
                                             'registered': registered})


def add_ship(request):
    form = ShipForm()

    if request.method == 'POST':
        form = ShipForm(request.POST)

        if form.is_valid():
            ship = form.save(commit=True)
            print('Created ship', ship)
            return redirect('/')
        else:
            print(form.errors)

    return render(request, 'add_ship.html', {'form': form})


def add_type(request):
    form = TypeForm()

    if request.method == 'POST':
        form = TypeForm(request.POST)

        if form.is_valid():
            type = form.save(commit=True)
            print('Created type', type)
            return redirect('/')
        else:
            print(form.errors)

    return render(request, 'add_type.html', {'form': form})


def add_series(request):
    form = SeriesForm()

    if request.method == 'POST':
        form = SeriesForm(request.POST)

        if form.is_valid():
            series = form.save(commit=True)
            print('Created series', series)
            return redirect('/')
        else:
            print(form.errors)

    return render(request, 'add_series.html', {'form': form})


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
    table = zip(t, c)
    context_dict = {'table': table}
    return render(request, 'counted.html', context_dict)


