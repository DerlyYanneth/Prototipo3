from django.shortcuts import render
from inventario.models import Moto
import plotly.express as px
import pandas as pd
# Create your views here.
def saludar(request):

    motos = Moto.objects.all() # Obtiene todas las instancias del modelo Moto desde la base de datos
    #Crea un DataFrame de pandas
    df = pd.DataFrame({
        "marca":["pulsar", "suzuki", "yamaha", "kawasaki", "starker", "vespa"],
        "cantidad":[4,3,1,5,6,2],
        "barrio":["Bosa", "El Dorado", "Santa Librada", "Brasilia", "Bosa", "Kennedy"],
        "mes":["enero", "agosto", "enero", "mayo", "noviembre", "octubre"]
    })
     # Crea un gráfico de barras usando Plotly Express basado en el DataFrame
    grafico = px.bar(df, x = "marca", y = "cantidad", color = "barrio")
    mihtml = grafico.to_html(full_html = False) # Convierte el gráfico a HTML

    meses = px.bar(df, x = "marca", y = "cantidad", color = "mes")
    miht = meses.to_html(full_html = False)
    #Define el contexto para pasar datos al template HTML
    context = {
        "nombre": "bienvenido a la gestión de ventas",
        "motos": motos,
        "grafica": mihtml,
        "me": miht
    
    }
    return render(request, "inventario/index.html", context)
    