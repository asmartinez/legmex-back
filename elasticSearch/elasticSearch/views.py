from django.http import HttpResponse
from django.shortcuts import render
from search.models import Car
from search.documents import CarDocument


def bootstrap(request):
    # doc_externo = loader.get_template('principal.html')
    # documento = doc_externo.render()
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

            for hit in s:
                print("Car name : {}, description {}".format(hit.name, hit.description))

            return render(request, "resultado_busqueda.html", {"query":s})
        
    else:
        mensaje = "No has introducido un valor"
    return HttpResponse(mensaje)
