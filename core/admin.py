from django.contrib import admin
# Aquí no registramos Portfolio, porque pertenece al app "portfolio"
from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "titulo_academico", "correo_electronico")
    search_fields = ("nombres", "apellidos", "correo_electronico")
