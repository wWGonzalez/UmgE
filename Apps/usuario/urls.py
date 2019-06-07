from django.conf.urls import url,include
from .views import RegistroUsuario
#from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^Registro$', RegistroUsuario.as_view(),name='Registro'),
]