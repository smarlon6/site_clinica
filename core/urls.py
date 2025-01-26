from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # Adicione a importação de 'include'


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('contas/', include('contas.urls')), # Adiciona contas
    path('', include('pages.urls')), # url do app 
    path('perfil/', include('perfil.urls')), # Adicionar
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)