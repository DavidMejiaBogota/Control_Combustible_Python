from django.shortcuts import render
from django.http import HttpResponse

def primera_vista(request):
    return HttpResponse("Hola mundo, desde el curso de Django para profesionales con: <b>J. David Mejía M.</b> ")


