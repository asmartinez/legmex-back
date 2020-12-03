from django.http import HttpResponse
from django.shortcuts import render
from search.models import Car
from search.documents import CarDocument


def bootstrap(request):

    #car = Car(
    #name="Car two",
    #color="green",
    #type=2,
    #description="A bonito car"
    #)
    #car.save()
    return render(request, "principal.html")

def buscar(request):

    if request.GET["prd"]:
        # mensaje="Articulo buscado: %r"%request.GET["prd"]
        producto = request.GET["prd"]

        if len(producto)>20:
            mensaje="Texto de busqueda demasiado largo"
        else:
            s = CarDocument.search().filter("term", color=producto)

            return render(request, "resultado_busqueda.html", {"query":s})
        
    else:
        mensaje = "No has introducido un valor"
    return HttpResponse(mensaje)

def subir(request):
    return render(request, "subir.html")

def respuesta(request):
    if request.GET["name"]:
        name = request.GET["name"]
        color = request.GET["color"]
        description = request.GET["description"]
        car = Car(
        name=name,
        color=color,
        type=2,
        description=description
        )
        car.save()
        return render(request, "respuesta.html", {"name":name, "color":color, "type":2, "description":description})