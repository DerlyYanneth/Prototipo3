from django.contrib import admin
from inventario.models import Moto
# Register your models here.
class InventarioAdmin(admin.ModelAdmin):
    list_display = ["marca", "cantidad", "barrio", "mes"] #Propiedad que especifica qué campos deben mostrarse en la lista de objetos del modelo en el panel de administración.
    list_search = ["barrio"] #Propiedad que especifica qué campos se pueden utilizar para buscar objetos en la lista del modelo en el panel de administración.
admin.site.register(Moto, InventarioAdmin)