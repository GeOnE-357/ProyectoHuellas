from django.db import models

# Calzado-----------------------------------------------------------------------------

class Calzado(models.Model):
    forma_sup = models.ForeignKey( 'Forma', default="", related_name="forma_sup", on_delete=models.PROTECT)
    forma_inf = models.ForeignKey( 'Forma', default="", related_name="forma_inf", on_delete=models.PROTECT)
    marca = models.ForeignKey( 'Marca', default="", on_delete=models.CASCADE )
    def __str__(self):
        return str(self.marca)+' '+str(self.forma_sup)+' '+ str(self.forma_inf)

def DirCalzado(instance, filename):
    # Se va a guardar en MEDIA_ROOT/Calzado/<calzado>/<nombre del archivo>
    return 'Calzado/{0}/{1}'.format(instance.calzado, filename)

class FotoCalzado(models.Model):
    calzado = models.ForeignKey('Calzado', default="",on_delete=models.CASCADE)
    frente = models.FileField(upload_to=DirCalzado)
    izquierda = models.FileField(upload_to=DirCalzado)
    atras = models.FileField(upload_to=DirCalzado)
    derecha = models.FileField(upload_to=DirCalzado)
    inferior= models.FileField(upload_to=DirCalzado)
    def __str__(self):
        return "Huella de  "+str(self.calzado)

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

def DirForma(instance, filename):
    return 'Forma/{0}/{1}'.format(instance.nombre, filename)

class Forma(models.Model):
    nombre = models.CharField(max_length=100)
    motivo = models.FileField(upload_to=DirForma)
    def __str__(self):
        return self.nombre