from django.shortcuts import render
from django.views.generic import *

from .models import *

class MarkList(ListView):
    template_name="ctrl_comb/mark.html"
    model=Mark
    context_object_name="obj"
    ordering=["descript"]