from .models import Calzado, Forma, Marca
import django_filters

class CalzadoFilter(django_filters.FilterSet):
    marca=django_filters.ModelChoiceFilter(queryset=Marca.objects.all(), label=False,)
    forma_sup=django_filters.ModelChoiceFilter(queryset=Forma.objects.all(), label=False,)
    forma_inf=django_filters.ModelChoiceFilter(queryset=Forma.objects.all(), label=False,)
    class Meta:
        model = Calzado
        fields = ['marca', 'forma_sup', 'forma_inf']