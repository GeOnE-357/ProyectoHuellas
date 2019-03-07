from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Calzado, FotoCalzado, Forma, Marca
from .filters import CalzadoFilter

def calzadoListar(request):
    calzado = Calzado.objects.all()
    filtro = CalzadoFilter(request.GET, queryset=calzado)
    return render(request, 'calzado/index.html', {'filtro':filtro})