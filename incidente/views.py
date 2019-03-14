from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Incidente, TipoIncidente, Parte, Cuerpo, ParteFoto, Distintivo, TipoDistintivo
from persona.models import Foto
from calzado.models import FotoCalzado
from .forms import IncidenteForm, ParteForm, TipoIncidenteForm
from .filters import IncidenteFilter

def incidenteListar(request):
	incidentes = Incidente.objects.all()
	filtro = IncidenteFilter(request.GET, queryset=incidentes)
	return render(request, 'incidente/index.html', {'filtro':filtro})

def incidenteCrear(request):
    if request.method == "POST":
    	if request.user.is_staff:
    		form = IncidenteForm(request.POST or None)
    		if form.is_valid():
	        	instance = form.save(commit=False)
	        	instance.save()
	        	tipo='pos'
	        	tit='INCIDENTE CREADO'
	        	men='El incidente a sido creado con exito.'
	        	return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    	else:
    		tipo='neg'
    		tit='ACCESO DENEGADO'
    		men='No tiene los permisos necesarios para realizar esta tarea.'
    		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
    	if request.user.is_staff:
    		form = IncidenteForm()
    	else:
    		tipo='neg'
    		tit='ACCESO DENEGADO'
    		men='No tiene los permisos necesarios para realizar esta tarea.'
    		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    return render(request, 'incidente/crear.html', {'form': form})

def incidenteDetalle(request, id):
    inci=get_object_or_404(Incidente, id=id)
    fotop=Foto.objects.get(id=inci.persona.id)
    fotoc=FotoCalzado.objects.get(id=inci.calzado.id)
    return render(request, 'incidente/detalle.html', {'inci':inci, 'fotop':fotop, 'fotoc':fotoc} )