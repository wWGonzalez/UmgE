


from django.conf.urls import url,include
from .views import EliminarEstudianteView,EstudianteList,IndexView,EstudianteView,crearEstudianteView,crearBusView,EditarBusView,EliminarBusView,BusList,LoginView,logout_view,EditarEstudianteView
#from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', IndexView.as_view(),name='home'),
	url(r'^Estudiante$', EstudianteView.as_view(),name='Estudiante'),
	url(r'^EstudianteList$', EstudianteList,name='EstudianteList'),
	url(r'^Bus$', BusList,name='BusList'),


	
	url(r'^AddEstudiante$', crearEstudianteView.as_view(),name='addEstudiante'),
	url(r'^AddBus$', crearBusView.as_view(),name='addBus'),
	url(r'^login$', LoginView.as_view(),name='login'),
	url(r'^logout$', logout_view,name='logout'),


	#url(r'^logout/$', auth_views.logout, {'next_page': 'App1:home'}, name='logout'),


	url(r'^EliminarEstudiante/(?P<pk>\d+)/$', EliminarEstudianteView.as_view(), name='DeleteEstudiante'),
	url(r'^EliminarBus/(?P<pk>\d+)/$', EliminarBusView.as_view(), name='DeleteBus'),
	

	
	url(r'^EditarBus/(?P<pk>\d+)/', EditarBusView.as_view(), name='EditarBus'),
	url(r'^EditarEstudiante/(?P<pk>\d+)/$', EditarEstudianteView.as_view(), name='EditarEstudiante'),



	

]