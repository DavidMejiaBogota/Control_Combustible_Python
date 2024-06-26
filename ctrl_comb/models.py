from django.db import models

'''
Se define una clase Mark que hereda de models.Model.
Esto significa que Mark es un modelo de Django y representará una tabla en la base de datos.'''
class Mark(models.Model): #Mark es el nombre de la tabla/modelo
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