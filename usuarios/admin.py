from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm,CustomUserCreationForm

UsuarioPersonalizado = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UsuarioPersonalizado
    list_display = [
        "email",
        "username",
        "is_superuser"
    ]

#Registar el usuario personalizado como el usuario que va a utilizar el admin
admin.site.register(UsuarioPersonalizado, CustomUserAdmin)