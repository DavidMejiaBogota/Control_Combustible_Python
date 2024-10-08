from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import RegistroUsuarioView

"""
Esta clase define pruebas unitarias para verificar la funcionalidad de creación de usuarios 
personalizados en Django. La prueba test_crear_usuario se encarga de crear un usuario utilizando
el método create_user del modelo de usuario personalizado y luego verifica si los atributos
del usuario creado son los esperados.
"""
class CustomUserTests(TestCase):
    #Crear usuario
    def test_crear_usurio(self):
        Usr = get_user_model()
        usr = Usr.objects.create_user(
            username = "marketbi",
            email = "auxiliar1@marketbi.co",
            password = "123",
            first_name = "debs"
        )
        #Verificar los atributos del usuario
        self.assertEqual(usr.username,"marketbi")
        self.assertEqual(usr.email,"auxiliar1@marketbi.co")
        self.assertTrue(usr.is_active)
        self.assertFalse(usr.is_staff)
        self.assertFalse(usr.is_superuser)

    def test_crear_superusuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_superuser(
            username = "adminmarketbi",
            email = "admin1@marketbi.co",
            password = "123",
            first_name = "debs"
        )
        #Verificar los atributos del usuario
        self.assertEqual(usr.username,"adminmarketbi")
        self.assertEqual(usr.email,"admin1@marketbi.co")
        self.assertTrue(usr.is_active)
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)

class RegistroUsuarioTest(TestCase):
    def setUp(self):
        url = reverse("usuarios:registro")
        self.response = self.client.get(url)
    
    #Prueba de plantilla
    def test_plantilla_registro(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,"usuarios/registro.html")
        self.assertContains(self.response,"Registrate")
        self.assertNotContains(self.response,"Bienvenido")
    
    #Prueba del formulario
    def test_registro_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response,"csrfmiddlewaretoken")

    #Pruebas de vista
    def test_registro_vista(self):
        view = resolve("/usuarios/registro/")
        self.assertEqual(view.func.__name__,RegistroUsuarioView.as_view().__name__)