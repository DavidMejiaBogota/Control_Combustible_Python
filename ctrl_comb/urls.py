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
    path("models/modal/<int:pk>",ModeloEditModal.as_view(),name="modelo_edit_modal"), #Actualiza/Edita el modelo del vehículo
    path("models/modal/new",ModeloNewModal.as_view(),name="modelo_new_modal"), #Crea el modelo del vehículos.
    path("models/dt",modelo_dt,name="modelo_dt"),

    #Rutas para le modelo Vehículo
    path("vehicles/",VehiculoList.as_view(),name="vehiculo_list"), #Lista los vehículos.
    path("vehicles/dt",vehiculo_dt,name="vehiculo_dt"), #Lista los vehículos.
    path("vehicles/new",VehiculoNewModal.as_view(),name="vehiculo_new"), #Crea el vehículo.
    path("vehicles/modal/<int:pk>",VehiculoEditModal.as_view(),name="vehiculo_edit"), #Permite editar/actualizar el vehículo.
    path("vehicles/delete/<int:pk>",VehiculoDelete.as_view(),name="vehiculo_delete"), #Perminte eliminar los vehículos.
]