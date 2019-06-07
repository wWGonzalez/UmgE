

from __future__ import unicode_literals
#from django.views.generic.edit import FormView



from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import EstudianteForm,BusForm
from .models import Estudiante,Bus

from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth import login
from django.views.generic import FormView
from django.contrib.auth import logout
from django.shortcuts import redirect



def EstudianteList(request):
	estudiantes = Estudiante.objects.all()
	context = {'estudiantes':estudiantes}
	return render(request,"Estudiante_listar.html",context)

#def EstudianteList(request):
#	obj = Estudiante.objects.all()
#	for entrada in obj:
#		obj_nombre = entrada.nombre
#		obj_direccion = entrada.direccion
#		obj_carne = entrada.carne

#	context = {
#	"obj":   obj,
#	"obj_nombre":obj_nombre,
#	"obj_direccion":obj_direccion,
#	"obj_carne":obj_carne,

#	}
#	return render(request,"Estudiante_listar.html",context)


def BusList(request):
	obj = Bus.objects.all()
	context = {'obj':obj}
	return render(request,"EstudianteAdmin_listar.html",context)





# Create your views here.

class IndexView(TemplateView):
	template_name='index.html'

class EstudianteView(TemplateView):
	template_name='Estudiante.html'


class LoginView(FormView):
	template_name='login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('App1:home')

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(LoginView, self).form_valid(form)


def logout_view(request):
	logout(request)
	return redirect('App1:home')








#class CrearEstudianteView(CreateView):
#template_name = 'crearEstudiante.html'
#form_class = EstudianteForm
#success_url = reverse_lazy('App1:home')

class crearEstudianteView(CreateView):
	template_name = 'crearEstudiante.html'
	form_class = EstudianteForm
	success_url = reverse_lazy('App1:home')


class crearBusView(CreateView):
	template_name = 'crearBus.html'
	form_class = BusForm
	success_url = reverse_lazy('App1:home')


	#Vistas para Editar
class EditarEstudianteView(UpdateView):
	template_name = 'crearEstudiante.html'
	model = Estudiante
	form_class = EstudianteForm
	success_url = reverse_lazy('App1:EstudianteList')

class EditarBusView(UpdateView):
	template_name = 'crearBus.html'
	model = Bus
	form_class = BusForm
	success_url = reverse_lazy('App1:home')



	#Vistaas para eliminar
class EliminarEstudianteView(DeleteView):
	template_name = 'Eliminar.html'
	model = Estudiante
	success_url = reverse_lazy('App1:EstudianteList')



class EliminarBusView(DeleteView):
	template_name = 'Eliminar.html'
	model = Bus
	success_url = reverse_lazy('App1:home')