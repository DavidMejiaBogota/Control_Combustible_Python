from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy

from .models import *
from .forms import *

class MarkList(ListView):
    template_name="ctrl_comb/mark.html"
    model=Mark
    context_object_name="obj"
    ordering=["descript"]

def mark_save(request):
    context={}
    template_name= "ctrl_comb/mark-list.html"

    if request.method=="POST":
        i = request.POST.get("id")
        d = request.POST.get("descript")
        o = None

        if i:
            o = Mark.objects.filter(id=i).first()
        else: 
            o = Mark.objects.filter(descript=d).first()
        
        if o:
            o.descript = d
            o.save()
        else:
            o = Mark.objects.create(descript = d)

    obj = Mark.objects.all().order_by("descript")
    r = Mark.objects.filter(id=o.id).first()
    context["obj"] = obj
    context["reg"] = r

    return render(request,template_name,context)

def mark_delete(request,pk):
    context={}
    template_name = "ctrl_comb/mark-list.html"

    o = Mark.objects.filter(id=pk).first()
    o.delete()

    obj = Mark.objects.all().order_by("descript")
    context["obj"] = obj

    return render(request,template_name,context)

def mark_edit(request,pk=None):
    context={}
    template_name = "ctrl_comb/mark-frm.html"

    if pk:
        o = Mark.objects.filter(id=pk).first()
        frm = MarkForm(instance=o)
    else:
        frm = MarkForm()
    
    context["frm"] = frm
    context["obj"] = o

    return render(request,template_name,context)

class ModeloList(ListView):
    template_name ="ctrl_comb/modelo.html"
    model=Modelo
    context_object_name = "obj"
    ordering = ["mark","descript"]

class ModeloNew(CreateView):
    model=Modelo
    template_name="ctrl_comb/modelo_form.html"
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list")

class ModeloEdit(UpdateView):
    model=Modelo
    template_name="ctrl_comb/modelo_form.html"
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list")

class ModeloDelete(DeleteView):
    model=Modelo
    template_name="bases/delete.html"
    context_object_name="obj"
    success_url=reverse_lazy("control:modelo_list")