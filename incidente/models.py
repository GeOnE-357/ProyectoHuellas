from django.db import models
from datetime import datetime, date, time, timedelta

class Incidente(models.Model):
	tipo=models.ForeignKey('TipoIncidente', on_delete=models.PROTECT)
	calzado=models.ForeignKey('calzado.Calzado', on_delete=models.PROTECT)
	persona=models.ForeignKey('persona.Persona', on_delete=models.PROTECT)
	detalle=models.CharField(max_length=200)
	fecha = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.tipo)+" por "+str(self.persona)+" el dia "+str(self.fecha.day)+"/"+str(self.fecha.month)+"/"+str(self.fecha.year)+"."

class TipoIncidente (models.Model):
	nombre=models.CharField(max_length=30)
	detalle=models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

def direc(instance, filename):
    # Se va a guardar en MEDIA_ROOT/Persona_<id_persona>/<fecha/nombre del archivo>
    fecha=date.today()
    dia=str(fecha.year)+'-'+str(fecha.month)+'-'+str(fecha.day)
    return 'Incidente_{0}/{1}/{2}'.format(instance.incidente_id, instance.nombre, filename)

class Parte (models.Model):
	incidente_id=models.ForeignKey('Incidente', on_delete=models.CASCADE)
	nombre=models.ForeignKey('Cuerpo', on_delete=models.PROTECT)
	lado=models.CharField(max_length=10)
	tipo= models.ForeignKey('TipoDistintivo', on_delete=models.PROTECT)
	detalle=models.CharField(null=True, max_length=100)
	foto = models.FileField(upload_to=direc)
	def __str__(self):
		return str(self.nombre)+" "+self.lado

class Cuerpo(models.Model):
	nombre=models.CharField(max_length=20)
	def __str__(self):
		return self.nombre

class TipoDistintivo(models.Model):
	nombre=models.CharField(max_length=15)

	def __str__(self):
		return self.nombre