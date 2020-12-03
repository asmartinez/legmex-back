from django.http import HttpResponse
from django.shortcuts import render


def bootstrap(request):
    # doc_externo = loader.get_template('principal.html')
    # documento = doc_externo.render()
    return render(request, "principal.html")

def buscar(request):

    if request.GET["prd"]:
        # mensaje="Articulo buscado: %r"%request.GET["prd"]
        producto = request.GET["prd"]

        if len(producto)>20:
            mensaje="Texto de busqueda demasiado largo"
        else:

            return render(request, "resultado_busqueda.html", {"query":producto})
        
    else:
        mensaje = "No has introducido un valor"
    return HttpResponse(mensaje)
