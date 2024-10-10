from django.db import models
from django.urls import reverse

from bases.models import ClaseModelo

'''
Se define una clase Mark que hereda de models.Model.
Esto significa que Mark es un modelo de Django y representará una tabla en la base de datos.
'''
class Mark(ClaseModelo): #Mark es el nombre de la tabla/modelo
    descript = models.CharField( #descript es el nombre del campo. models.CharField: Es un tipo de campo para almacenar cadenas de texto.
        max_length=50, #longitud maxima del campo
        unique=True, #indicador de que serán elementos únicos, no habrán dos con el mismo nombre.
    )

    def __str__(self): #Este método define como se presentará el objeto 'Mark'  como una cadena de texto. Esto es útil para reprsentaciones legibles en la administración de Django y  entoras interfaces
        return self.descript #Este método devuleve el valor del campo 'descript'. Por lo tanto, cuando se imprima una instancia de 'Mark', ase mostrará el valor del campo 'desript'.


    class Meta: #Clase Meta
        verbose_name = 'Marca' #Descripción singular del modelo
        verbose_name_plural = 'Marcas' #Descripción del plural del modelo
        ordering = ['descript'] #Ordenamiento del modelo. El ordenamiento se basará en el campo 'descript'

class Modelo(ClaseModelo):
    descript = models.CharField(
        max_length=50,
        db_comment = "Descripción del Modelo de Vehículo",
    )

    mark = models.ForeignKey(Mark,on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.mark} - {self.descript}"
    
    class Meta:
        verbose_name_plural = "Modelos"
        db_table_comment = "Modelos de Vehículos"
        permissions = [
            ("permiso_especial","Puede leer y editar Modelos"),
        ]

#Modelo para la creación de vehículos

class Vehiculo(ClaseModelo):
    modelo = models.ForeignKey(Modelo, on_delete=models.RESTRICT)
    register = models.CharField(max_length=50,db_column="Matricula Vehículo",help_text="Matricula Vehículo")
    year =  models.PositiveSmallIntegerField(help_text="Año del Vehículo")

    def __str__(self):
        return self.register
    
    def get_absolute_url(self):
        return reverse("vehiculo_edit",kwargs={'pk':self.pk})
    
    class Meta:
        verbose_name_plural = "Vehículos"
        db_table_comment = "Vehículos"
