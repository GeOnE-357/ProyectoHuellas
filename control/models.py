from django.db import models

class Log(models.Model):
	dni = models.CharField(max_length=20)
	nombre = models.CharField(max_length=20)
	accion = models.CharField(max_length=20)
	tabla = models.CharField(max_length=20)
	objeto = models.IntegerField()
	fecha = models.DateTimeField(null=True)

	class Meta:
		db_table = "control_logs"

	def __str__(self):
		return "El usuario: "+self.dni+" - "+self.nombre+" | Realizo la accion: "+self.accion+" en la tabla: "+self.tabla+" en el objeto Id: "+str(self.objeto)+", el dia "+str(self.fecha)

