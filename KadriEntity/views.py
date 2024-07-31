from django.shortcuts import render
from django.urls import path,include
from .Controlers import viewsDolznosty,viewsZarplata,viewsSotrudniki


route_toKadri= [
    path("Dolznosty/", include(viewsDolznosty.route_toKadriDolznosty)),
    path("Zarplata/", include(viewsZarplata.route_toKadriZarplata)),
    path("Sotrudniki/", include(viewsSotrudniki.route_toKadriSotrudniki)),
]