from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Incidente, TipoIncidente, Parte, Cuerpo, ParteFoto, Distintivo, TipoDistintivo
from .forms import IncidenteForm, ParteForm, TipoIncidenteForm
from .filters import IncidenteFilter

def incidenteListar(request):
	incidentes = Incidente.objects.all()
	filtro = IncidenteFilter(request.GET, queryset=incidentes)
	return render(request, 'incidente/index.html', {'filtro':filtro})