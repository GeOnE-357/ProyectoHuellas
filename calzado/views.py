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

def calzadoMarca(request):
    if request.method == "POST":
        if request.user.is_staff:
            mar=Marca.objects.all()
            ban=0
            for m in mar:
                if request.POST["nombre"] == m.nombre:
                    ban=1
            if ban == 0:
                form = MarcaForm(request.POST or None)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.save()
                    tipo='pos'
                    tit='MARCA CREADA'
                    men='La Marca ah sido creada con exito.'
                    return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
            else:
                tipo='neg'
                tit='MARCA YA CREADA'
                men='La Marca ya existe en la base de datos.'
                return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
        if request.user.is_staff:
            form = MarcaForm()
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    return render(request, 'calzado/marca.html', {'form': form})

def calzadoMotivo(request):
    if request.method == "POST":
        if request.user.is_staff:
            mot=Forma.objects.all()
            ban=0
            for m in mot:
                if request.POST["nombre"] == m.nombre:
                    ban=1
            if ban == 0:
                form = FormaForm(request.POST or None)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.save()
                    tipo='pos'
                    tit='MOTIVO CREADO'
                    men='El Motivo ah sido creada con exito.'
                    return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
            else:
                tipo='neg'
                tit='MOTIVO YA CREADO'
                men='El Motivo ya existe en la base de datos.'
                return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
        if request.user.is_staff:
            form = FormaForm()
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    return render(request, 'calzado/motivo.html', {'form': form})

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

def fotoEditar(request, id):
    if request.method == "POST":
        if request.user.is_staff:
            foto=get_object_or_404(FotoCalzado, id=id)
            form=FotoCalzadoForm(request.POST, request.FILES, instance=foto)
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
            foto=get_object_or_404(FotoCalzado, id=id)
            form = FotoCalzadoForm(instance=foto)
        else:
            tipo='neg'
            tit='ACCESO DENEGADO'
            men='No tiene los permisos necesarios para realizar esta tarea.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
        return render(request, 'calzado/fotos.html', {'form': form})

def calzadoDetalle(request, id):
    calzado = get_object_or_404(Calzado,id=id)
    foto= FotoCalzado.objects.all().filter(calzado=id)
    return render(request, 'calzado/detalle.html', {'calzado': calzado, 'foto':foto})