from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

"""
Esta clase define pruebas unitarias para verificar la funcionalidad de creación de usuarios 
personalizados en Django. La prueba test_crear_usuario se encarga de crear un usuario utilizando
el método create_user del modelo de usuario personalizado y luego verifica si los atributos
del usuario creado son los esperados.
"""
class CustomUserTest(TestCase):
    #Crear usuario
    def test_crear_usurio(self):
        Usr = get_user_model()
        usr = Usr.objects.create_user(
            username = "marketbi",
            email = "auxiliar1@marketbi.co",
            password = "123"
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
            password = "123"
        )
        #Verificar los atributos del usuario
        self.assertEqual(usr.username,"adminmarketbi")
        self.assertEqual(usr.email,"admin1@marketbi.co")
        self.assertTrue(usr.is_active)
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)