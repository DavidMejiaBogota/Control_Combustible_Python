from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE,related_name="+") #uc=ususarioCrea
    fc = models.DateTimeField(auto_now_add=True) #fc=fechaCreación
    um = models.ForeignKey(User, on_delete=models.SET_NULL,related_name="+",blank=True,null=True) #um=usuarioModifica
    fm = models.DateTimeField(auto_now=True) #fechaModificacion

    class Meta:
        abstract = True