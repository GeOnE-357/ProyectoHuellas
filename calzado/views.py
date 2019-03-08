from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Calzado, FotoCalzado, Forma, Marca
from .filters import CalzadoFilter
from .forms import CalzadoForm, FotoCalzadoForm, MarcaForm, FormaForm 

def calzadoListar(request):
    calzado = Calzado.objects.all()
    filtro = CalzadoFilter(request.GET, queryset=calzado)
    return render(request, 'calzado/index.html', {'filtro':filtro})

def calzadoCrear(request):
    if request.method == "POST":
    	if request.user.is_staff:
    		form = CalzadoForm(request.POST or None)
    		if form.is_valid():
	        	instance = form.save(commit=False)
	        	instance.save()
	        	c=Calzado.objects.all().last().id
	        	return redirect('calzado-foto', id=c)
    	else:
    		tipo='neg'
    		tit='ACCESO DENEGADO'
    		men='No tiene los permisos necesarios para realizar esta tarea.'
    		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
    	if request.user.is_staff:
    		form = CalzadoForm()
    	else:
    		tipo='neg'
    		tit='ACCESO DENEGADO'
    		men='No tiene los permisos necesarios para realizar esta tarea.'
    		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    return render(request, 'calzado/crear.html', {'form': form})

def calzadoFoto(request, id):
	if FotoCalzado.objects.all().filter(calzado=id):
		tipo='pos'
		tit='FOTO CALZADO'
		men='Las Fotos del calzado ya fueron creadas anteriormente.'
		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
	if request.method == "POST":
		if request.user.is_staff:
			form=FotoCalzadoForm(request.POST, request.FILES)
			if form.is_valid():
				instance = form.save(commit=False)
				c=Calzado.objects.get(id=id)
				instance.calzado=c
				instance.save()
				tipo='pos'
				tit='CALZADO CREADO'
				men='El Calzado a sido creada con exito.'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
	else:
		if request.user.is_staff:
			form = FotoCalzadoForm()
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
	return render(request, 'calzado/fotos.html', {'form': form})

def calzadoEditar(request, id):
    if request.method == "POST":
    	if request.user.is_staff:
    		calzado=get_object_or_404(Calzado, id=id)
    		form = CalzadoForm(request.POST, instance=calzado)
    		if form.is_valid():
	        	instance = form.save(commit=False)
	        	instance.save()
	        	tipo='pos'
	        	tit='CALZADO EDITADO'
	        	men='El Calzado a sido editado con exito.'
	        	return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    	else:
    		tipo='neg'
    		tit='ACCESO DENEGADO'
    		men='No tiene los permisos necesarios para realizar esta tarea.'
    		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})	
    else:
    	if request.user.is_staff:
    		calzado=get_object_or_404(Calzado, id=id)
    		form = CalzadoForm(instance=calzado)
    	else:
    		tipo='neg'
    		tit='ACCESO DENEGADO'
    		men='No tiene los permisos necesarios para realizar esta tarea.'
    		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    return render(request, 'calzado/crear.html', {'form': form})

def calzadoDetalle(request, id):
    calzado = get_object_or_404(Calzado,id=id)
    foto= FotoCalzado.objects.all().filter(calzado=id)
    return render(request, 'calzado/detalle.html', {'calzado': calzado, 'foto':foto})