from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Incidente, TipoIncidente, Parte, Cuerpo, TipoDistintivo
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

def incidenteTipo(request):
	if request.method == "POST":
		if request.user.is_staff:
			form = TipoIncidenteForm(request.POST or None)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				tipo='pos'
				tit='TIPO CREADO'
				men='El tipo de incidente a sido creado con exito.'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
	else:
		if request.user.is_staff:
			form = TipoIncidenteForm()
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
	return render(request, 'incidente/crear.html', {'form': form})

def incidenteDetalle(request, id):
	inci=get_object_or_404(Incidente, id=id)
	fotop=Foto.objects.get(id=inci.persona.id)
	parte=Parte.objects.all().filter(incidente_id=id)
	return render(request, 'incidente/detalle.html', {'inci':inci, 'fotop':fotop, 'parte':parte} )

def cuerpoCrear(request, id):
	if request.method == "POST":
		if request.user.is_staff:
			form = ParteForm(request.POST, request.FILES)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.incidente_id=Incidente.objects.get(id=id)
				instance.save()
				tipo='pos'
				tit='DETALLE CUERPO CREADO'
				men='El detalle a sido creado con exito.'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
	else:
		if request.user.is_staff:
			form = ParteForm()
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
	return render(request, 'incidente/cuerpo.html', {'form': form})

def incidenteEstadistica(request):
	if request.user.is_staff:
		incidentes = Incidente.objects.all().order_by("tipo")
		tipo=TipoIncidente.objects.all().order_by("id")
		total=incidentes.count()
		lista=[]
		for t in tipo:
			inci=[]
			inci.append(t.nombre)
			cant=0
			for i in incidentes:
				if i.tipo.id==t.id:
					cant+=1
			inci.append(cant)
			if inci[1] > 0:
				por=cant*100/total
				inci.append(str(por)+"%")
				lista.append(inci)
		return render(request, 'incidente/estadistica.html', {'lista':lista})
	else:
		tipo='neg'
		tit='ACCESO DENEGADO'
		men='No tiene los permisos necesarios para realizar esta tarea.'
		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})