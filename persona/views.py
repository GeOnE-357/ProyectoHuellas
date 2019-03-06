from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from datetime import datetime, date, time, timedelta
from persona.models import Persona, InfoComp, Fisico, Foto, BarbaBigote, BocaContorno, BocaEspesor, CabelloColor, CabelloLargo, CejaDireccion, CejaPilosidad, OjoColor, OjoForma, OjoTono, Tez, Menton, ManoDeUso, Nariz, EstadoCivil
from persona.forms import PersonaForm, InfoForm, FisicoForm, FotosForm
from persona.filters import PersonaFilter

def personaCrear(request):
    if request.method == "POST":
    	if request.user.is_staff:
    		form = PersonaForm(request.POST or None)
    		if form.is_valid():
	        	instance = form.save(commit=False)
	        	instance.save()
	        	p=Persona.objects.all().last().id
	        	return redirect('info-crear', id=p)
    	else:
    		tipo='neg'
    		tit='ACCESO DENEGADO'
    		men='No tiene los permisos necesarios para realizar esta tarea.'
    		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
        form = PersonaForm()
    return render(request, 'persona/crear.html', {'form': form})

def infoCrear(request, id):
    if request.method == "POST":
    	if request.user.is_staff:
    		form = InfoForm(request.POST or None)
    		if form.is_valid():
	        	instance = form.save(commit=False)
	        	p=Persona.objects.get(id=id)
	        	instance.id_persona=p
	        	instance.save()
	        	instance.save()
	        	return redirect('fisico-crear', id=id)
    	else:
    		tipo='neg'
    		tit='ACCESO DENEGADO'
    		men='No tiene los permisos necesarios para realizar esta tarea.'
    		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
        form = InfoForm()
    return render(request, 'persona/info.html', {'form': form})

def fisicoCrear(request, id):
    if request.method == "POST":
        if request.user.is_staff:
            form = FisicoForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                p=Persona.objects.get(id=id)
                instance.id_persona=p
                instance.save()
                instance.save()
                return redirect('foto-crear', id=id)
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
        form = FisicoForm()
    return render(request, 'persona/info.html', {'form': form})

def fotosCrear(request, id):
    if request.method == "POST":
        if request.user.is_staff:
            form = FotosForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                p=Persona.objects.get(id=id)
                instance.id_persona=p
                instance.save()
                tipo='pos'
                tit='PERSONA CREADA'
                men='La persona a sido creada con exito.'
                return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
                
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
        form = FotosForm()
    return render(request, 'persona/fotos.html', {'form': form})

def personaListar(request):
    personas = Persona.objects.all()
    filtro = PersonaFilter(request.GET, queryset=personas)
    return render(request, 'persona/index.html', {'filtro':filtro})

def personaDetalle(request, id):
    prin=Persona.objects.get(id=id)            
    edad=date.today().year-prin.fnac.year
    if date.today().month < prin.fnac.month:
        edad-=1
    secu=InfoComp.objects.get(id=id)
    fisi=Fisico.objects.get(id=id)
    foto=Foto.objects.all().order_by('fecha').filter(id_persona=id).last()
    print(foto)
    return render(request, 'persona/detalle.html', {'prin':prin, 'edad':edad ,'secu':secu, 'fisi':fisi, 'foto':foto} )