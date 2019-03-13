from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Incidente, TipoIncidente, Parte, ParteLista, ParteFoto, Distintivo, Tipo
from .forms import