from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.base, name='base'),
    path('home/', core_views.home, name='home'),
    path('about/', core_views.acerca_de, name='about'),   # dinámico con modelo Persona y plantilla about.html
    path('contacto/', core_views.contacto, name='contacto'),
    path('portafolio/', portfolio_views.portafolio, name='portafolio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
