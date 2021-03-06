from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from datetime import datetime, date, time, timedelta
from .models import Incidente, TipoIncidente, Parte, Cuerpo, TipoDistintivo
from persona.models import Foto
from calzado.models import FotoCalzado
from .forms import IncidenteForm, ParteForm, TipoIncidenteForm, PeriodoForm
from .filters import IncidenteFilter

def incidenteListar(request):
    incidentes = Incidente.objects.all()
    filtro = IncidenteFilter(request.GET, queryset=incidentes)
    return render(request, 'incidente/index.html', {'filtro':filtro})

def incidenteCrear(request):
    titu="Registrar Incidente"
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
    return render(request, 'incidente/crear.html', {'form': form, 'titu':titu})

def incidenteTipo(request):
    titu="Registrar Tipo de Incidente"
    if request.method == "POST":
        if request.user.is_staff:
            tip=TipoIncidente.objects.all()
            ban=0
            for t in tip:
                if request.POST["nombre"] == t.nombre:
                    ban=1
            if ban == 0:
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
                tit='TIPO YA CREADO'
                men='El Tipo de Incidente ya existe en la base de datos.'
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
    return render(request, 'incidente/crear.html', {'form': form, 'titu':titu})

def incidenteDetalle(request, id):
    inci=get_object_or_404(Incidente, id=id)
    fotop=Foto.objects.get(id=inci.persona.id)
    parte=Parte.objects.all().filter(incidente_id=id)
    return render(request, 'incidente/detalle.html', {'inci':inci, 'fotop':fotop, 'parte':parte} )

def cuerpoCrear(request, id):
    titu="Registrar Marcas Particulares"
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
    return render(request, 'incidente/cuerpo.html', {'form': form, 'titu':titu})

def incidenteEstadistica(request):
    if request.user.is_staff:
        if request.method == "GET":
            form = PeriodoForm(request.GET)
            if form.is_valid():
                inicio = form.cleaned_data['inicio']
                fin = form.cleaned_data['fin']
                incidentes = Incidente.objects.all().order_by("tipo").filter(fecha__gt=inicio, fecha__lt=fin)
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
            else:
                form=PeriodoForm()
                lista=[]
            return render(request, 'incidente/estadistica.html', {'lista':lista, 'form':form})
    else:
        tipo='neg'
        tit='ACCESO DENEGADO'
        men='No tiene los permisos necesarios para realizar esta tarea.'
        return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})