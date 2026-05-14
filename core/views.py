from django.shortcuts import render
from .models import Persona   # Importamos el modelo Persona

# Página principal
def home(request):
    return render(request, 'core/home.html')

# Página "Acerca de" (estática, si aún la usas)
def about(request):
    return render(request, 'core/about.html')

# Base layout
def base(request):
    return render(request, 'core/base.html')

# Portafolio (usa la app portfolio para proyectos)
def portafolio(request):
    return render(request, 'core/portafolio.html')

# Página de contacto
def contacto(request):
    return render(request, 'core/contacto.html')

# Página dinámica "Acerca de mí" con datos del modelo Persona
def acerca_de(request):
    persona = Persona.objects.first()  # Obtiene el único registro
    return render(request, "core/about.html", {"persona": persona})

