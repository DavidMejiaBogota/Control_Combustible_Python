from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse_lazy

from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class MixinFormInvalid:
    def form_invalid(self,form):
        response = super().form_invalid(form)
        if is_ajax(request=self.request):
            return JsonResponse(form.errors,status=400)
        else:
            return response

class SinAutorizacion(LoginRequiredMixin,PermissionRequiredMixin,MixinFormInvalid):
    login_url = "bases:login"
    raise_exception = False
    redirect_field_name = "redirect_to"
    
    def handle_no_permission(self):
        if not self.request.user == AnonymousUser():
            self.login_url = "pages:forbidden"
        return HttpResponseRedirect(reverse_lazy(self.login_url))

def primera_vista(request):
    return HttpResponse("Hola mundo, desde el curso de Django para profesionales con: <b>J. David Mejía M.</b> ")

class HomeView(TemplateView):
    template_name = "bases/home.html"

class MixinSaveUser:
    def form_valid(self,form):
        print(f"********{form.instance.id} ---- {self.request.user.id}************")

        if form.instance.id:
            form.instance.um = self.request.user
        else:
            form.instance.uc = self.request.user
        return super().form_valid(form)