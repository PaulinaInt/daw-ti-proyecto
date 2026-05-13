from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, template_name='core/home.html')
def about(request):
    return render(request, template_name='core/about.html')
def base(request):
    return render(request, template_name='core/base.html')
def portafolio(request):
    return render(request, template_name='core/portafolio.html')
def contacto(request):
    return render(request, template_name='core/contacto.html')