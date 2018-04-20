"""starwars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lists import views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('ships/', include('lists.urls'), name='ships'),
    path('imperial_crushers/', views.crushers, name='imperial_crushers'),
    path('long_ships/', views.long, name='long_ships'),
    path('imperial_ships/', views.count, name='imperial_ships'),

    path('add_type/', views.add_type, name='add_type'),
    path('add_series/', views.add_series, name='add_series'),
    path('add_ship/', views.add_ship, name='add_ship'),

    path('registration/', views.register, name='registration'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

