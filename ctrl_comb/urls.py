from django.urls import path
from .views import *

urlpatterns = [
    #Rutas para el modelo Marcas
    path("mark/",MarkList.as_view(),name="mark_list"), #Lista las marcas de vehículos.
    path("mark/save",mark_save,name="mark_save"), #Crea las marcas de vehículos.
    path("mark/delete/<int:pk>",mark_delete,name="mark_delete"), #Eliminar las marcas de vehículos
    path("mark/edit/<int:pk>",mark_edit,name="mark_edit"), #Edita las marcas de vehículos.

    #Rutas para el modelo Modelos
    path("models/",ModeloList.as_view(),name="modelo_list"), #Lista los modelos de vehículos.
    path("models/new",ModeloNew.as_view(),name="modelo_new"), #Crea el modelo del vehículos.
    path("models/<int:pk>",ModeloEdit.as_view(),name="modelo_edit"), #Actualiza/Edita el modelo del vehículo
    path("models/delete/<int:pk>",ModeloDelete.as_view(),name="modelo_delete"), #Elimina los modelos de vehículos

]