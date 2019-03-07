from .models import Calzado, Forma
import django_filters

class CalzadoFilter(django_filters.FilterSet):
    nombre=django_filters.CharFilter(label=False,)
    forma_sup=django_filters.ModelChoiceFilter(queryset=Forma.objects.all(), label=False,)
    forma_inf=django_filters.ModelChoiceFilter(queryset=Forma.objects.all(), label=False,)
    class Meta:
        model = Calzado
        fields = ['nombre', 'forma_sup', 'forma_inf']