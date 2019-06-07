from django import forms
from .models import Estudiante,Bus

class EstudianteForm(forms.ModelForm):
	 class Meta:
	 	model = Estudiante
	 	fields = '__all__'


	 	
class BusForm(forms.ModelForm):
	 class Meta:
	 	model = Bus
	 	fields = '__all__'