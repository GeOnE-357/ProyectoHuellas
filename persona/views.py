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
    if InfoComp.objects.all().filter(id_persona=id):
        return redirect('fisico-crear', id=id)
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
    if Fisico.objects.all().filter(id_persona=id):
        return redirect('foto-crear', id=id)
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
    return render(request, 'persona/fisico.html', {'form': form})

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
        if request.user.is_staff:
            form = FotosForm()
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    return render(request, 'persona/fotos.html', {'form': form})

def personaListar(request):
    personas = Persona.objects.all()
    filtro = PersonaFilter(request.GET, queryset=personas)
    return render(request, 'persona/index.html', {'filtro':filtro})

def personaDetalle(request, id):
    prin=get_object_or_404(Persona, id=id)            
    edad=date.today().year-prin.fnac.year
    if date.today().month < prin.fnac.month:
        edad-=1
    secu=InfoComp.objects.all().filter(id_persona=id)
    fisi=Fisico.objects.all().filter(id_persona=id)
    foto=Foto.objects.all().order_by('fecha').filter(id_persona=id).last()
    return render(request, 'persona/detalle.html', {'prin':prin, 'edad':edad ,'secu':secu, 'fisi':fisi, 'foto':foto} )


def personaEditar(request, id):
    if request.method=="POST":
        if request.user.is_staff:
            persona=get_object_or_404(Persona, id=id)
            form = PersonaForm(request.POST, instance=persona)
            if form.is_valid():
                form.save(commit=False)
                form.save()
                tipo='pos'
                tit='PERSONA EDITADA'
                men='La Persona ha sido editada exitosamente.'
                return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
        if request.user.is_staff:
            persona=get_object_or_404(Persona, id=id)
            form = PersonaForm(instance=persona)
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    return render(request, 'persona/crear.html', {'form':form})

def infoEditar(request, id):
    if request.method=="POST":
        if request.user.is_staff:
            persona=get_object_or_404(InfoComp, id_persona=id)
            form = InfoForm(request.POST, instance=persona)
            if form.is_valid():
                form.save(commit=False)
                form.save()
                tipo='pos'
                tit='INFORMACION EDITADA'
                men='La Informacion Complementaria ha sido editada exitosamente.'
                return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
        if request.user.is_staff:
            persona=get_object_or_404(InfoComp, id_persona=id)
            form = InfoForm(instance=persona)
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    return render(request, 'persona/info.html', {'form':form})

def fisicoEditar(request, id):
    if request.method=="POST":
        if request.user.is_staff:
            persona=get_object_or_404(Fisico, id_persona=id)
            form = FisicoForm(request.POST, instance=persona)
            if form.is_valid():
                form.save(commit=False)
                form.save()
                tipo='pos'
                tit='FISICO EDITADO'
                men='El Fisico ha sido editada exitosamente.'
                return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
        if request.user.is_staff:
            persona=get_object_or_404(Fisico, id_persona=id)
            form = FisicoForm(instance=persona)
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    return render(request, 'persona/fisico.html', {'form':form})

def fotoHistorial(request, id):
    if request.user.is_staff:
        foto=Foto.objects.all().order_by('fecha').filter(id_persona=id).reverse()
        return render(request, 'persona/historial.html', {'foto':foto})
    else:
        tipo='neg'
        tit='ACCESO DENEGADO'
        men='No tiene los permisos necesarios para realizar esta tarea.'
        return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})