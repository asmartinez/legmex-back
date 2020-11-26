from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def saludo(request): #primera vista

    nombre = "Juan"
    apellido = "Diaz"
    ahora = datetime.datetime.now()
    lista = ["php","django","html","elasticsearch"]
    # lista = []

    # doc_externo = open("/home/danytorres/buscador-elasticSearch/elasticSearch/elasticSearch/plantillas/miplantilla.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close()

    # doc_externo = loader.get_template('miplantilla.html') > carga la plantilla, se tiene que especificar la carpeta donde estan las plantillas en el documento settings.py en la seccion templates > DIR 

    ctx = {"nombre_persona":nombre, "apellido_persona":apellido, "tiempo":ahora, "temas":lista} # contexto de la plantilla, de aqui se trae las variables que necesita la plantilla para mostrar su informacion 
    # documento = doc_externo.render(ctx) > Renderiza la plantilla con el contexto dado

    return render(request, "miplantilla.html", ctx)

def despedida(request):
    return HttpResponse("Hasta luego alumnos django")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>Fecha y hora actuales %s</h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    #edadActual = 18 
    periodo = agno - 2020
    edadFutura = edad + periodo
    documento = "<html><body><h2>en el año %s tendras %s años</h2></body></html>" %(agno, edadFutura)
    return HttpResponse(documento)

def bootstrap(request):
    # doc_externo = loader.get_template('principal.html')
    # documento = doc_externo.render()
    return render(request, "principal.html")
