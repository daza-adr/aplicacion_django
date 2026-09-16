from django.shortcuts import render
from .models import Mensaje

def contacto(request):
    if request.method == "POST":
        mensaje = Mensaje(
            nombre=request.POST["nombre"],
            correo=request.POST["correo"],
            mensaje=request.POST["mensaje"]
        )
        mensaje.save()
        return render(request, "gracias.html")

    return render(request, "contacto.html")