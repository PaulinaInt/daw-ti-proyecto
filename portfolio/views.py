from django.shortcuts import render
from .models import Portfolio

def portafolio(request):
    # Obtiene todos los objetos de la tabla Portfolio ordenados por fecha de creación
    proyectos = Portfolio.objects.all().order_by('-created')
    # Renderiza la plantilla y pasa los proyectos al contexto
    return render(request, 'core/portafolio.html', {'proyectos': proyectos})
