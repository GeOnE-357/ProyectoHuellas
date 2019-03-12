from django.db import models
from datetime import datetime, date, time, timedelta
from django.db import models

# Persona-----------------------------------------------------------------------------
class Persona(models.Model):
    #--> Informacion Personal <--
    registro = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    apellido2 = models.CharField(blank=True, max_length=100)
    apodo = models.CharField(blank=True, max_length=100)
    domicilio = models.CharField(max_length=100)
    domicilio_laboral = models.CharField(blank=True, max_length=100)
    fnac = models.DateField(auto_now=False, auto_now_add=False)
    dni = models.BigIntegerField()
    sexo = models.ForeignKey('Sexo',on_delete=models.PROTECT)
    nacionalidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    lugar_residencia = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
 
class InfoComp(models.Model):
    #--> Informacion Complementaria <--
    id_persona = models.ForeignKey('Persona', on_delete=models.CASCADE)
    ocupacion = models.CharField(blank=True, max_length=100)
    nombre_padre = models.CharField(max_length=100)
    padre_vive = models.BooleanField(default=True, blank=True)
    nombre_madre = models.CharField(max_length=100)
    madre_vive = models.BooleanField(default=True, blank=True)
    conyugue = models.CharField(blank=True, max_length=100)
    conyugue_vive = models.BooleanField(default=True, blank=True)
    telefono = models.BigIntegerField(blank=True)
    celular = models.BigIntegerField(blank=True)
    estado_civil = models.ForeignKey('EstadoCivil', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Infomacion de: '+str(self.id_persona)

class Fisico(models.Model):
    #--> Descripcion Fisica <--
    id_persona = models.ForeignKey('Persona', on_delete=models.CASCADE)
    altura = models.FloatField(max_length=10)
    peso = models.FloatField(max_length=10)
    tez = models.ForeignKey('Tez',verbose_name="Color de Piel",on_delete=models.PROTECT)
    ojo_color = models.ForeignKey(
        'OjoColor', verbose_name="Color de Ojos",on_delete=models.PROTECT)
    ojo_forma = models.ForeignKey(
        'OjoForma', verbose_name="Forma de Ojos",on_delete=models.PROTECT)
    ojo_tono = models.ForeignKey(
        'OjoTono', verbose_name="Tono de Ojos",on_delete=models.PROTECT)
    cabello_color = models.ForeignKey('CabelloColor', on_delete=models.PROTECT)
    cabello_largo = models.ForeignKey('CabelloLargo', on_delete=models.PROTECT)
    barba_bigote = models.ForeignKey('BarbaBigote', on_delete=models.PROTECT)
    ceja_pilosidad = models.ForeignKey('CejaPilosidad', on_delete=models.PROTECT)
    ceja_direccion = models.ForeignKey('CejaDireccion', on_delete=models.PROTECT)
    menton = models.ForeignKey('Menton', on_delete=models.PROTECT)
    mano_de_uso = models.ForeignKey('ManoDeUso', on_delete=models.PROTECT)
    boca_contorno = models.ForeignKey('BocaContorno', on_delete=models.PROTECT)
    boca_espesor = models.ForeignKey('BocaEspesor', on_delete=models.PROTECT)
    nariz = models.ForeignKey('Nariz', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Datos Fisicos de:'+str(self.id_persona)

def directorio(instance, filename):
    # Se va a guardar en MEDIA_ROOT/Persona_<id_persona>/<fecha/nombre del archivo>
    dia=str(instance.fecha.year)+'-'+str(instance.fecha.month)+'-'+str(instance.fecha.day)
    return 'Persona_{0}/{1}/{2}'.format(instance.id_persona, dia, filename)

class Foto(models.Model):
    #--> Fotos Persona  <--    
    id_persona = models.ForeignKey('Persona', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cara = models.FileField(upload_to=directorio)
    frente = models.FileField(upload_to=directorio)
    izquierda = models.FileField(upload_to=directorio)
    atras = models.FileField(upload_to=directorio)
    derecha = models.FileField(upload_to=directorio)

    def __str__(self):
        dia=str(self.fecha.day)+'/'+str(self.fecha.month)+'/'+str(self.fecha.year)
        return 'Foto de '+str(self.id_persona)+" del "+dia


# Tablas de Info Persona-----------------------------------------------------------------------------

class Tez(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Sexo (models.Model):
    genero = models.CharField(max_length=10)
    def __str__(self):
            return self.genero

class Nariz(models.Model):
    forma = models.CharField(max_length=100)

    def __str__(self):
        return self.forma

class OjoColor(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class OjoForma(models.Model):
    forma = models.CharField(max_length=100)

    def __str__(self):
        return self.forma

class OjoTono(models.Model):
    tono = models.CharField(max_length=100)

    def __str__(self):
        return self.tono

class CabelloColor(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class CabelloLargo(models.Model):
    largo = models.CharField(max_length=100)

    def __str__(self):
        return self.largo

class BarbaBigote(models.Model):
    barba_bigote = models.CharField(max_length=100)

    def __str__(self):
        return self.barba_bigote

class CejaPilosidad(models.Model):
    pilosidad = models.CharField(max_length=100)

    def __str__(self):
        return self.pilosidad

class CejaDireccion(models.Model):
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.direccion

class BocaContorno(models.Model):
    contorno = models.CharField(max_length=100)

    def __str__(self):
        return self.contorno

class BocaEspesor(models.Model):
    espesor = models.CharField(max_length=100)

    def __str__(self):
        return self.espesor

class Menton(models.Model):
    forma = models.CharField(max_length=100)

    def __str__(self):
        return self.forma

class ManoDeUso(models.Model):
    uso = models.CharField(max_length=100)
    def __str__(self):
        return self.uso

class EstadoCivil(models.Model):
    estado = models.CharField(max_length=100)
    def __str__(self):
        return self.estado