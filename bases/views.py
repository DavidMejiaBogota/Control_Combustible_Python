from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *

def primera_vista(request):
    return HttpResponse("Hola mundo, desde el curso de Django para profesionales con: <b>J. David Mejía M.</b> ")

class HomeView(TemplateView):
    template_name = "bases/home.html"
