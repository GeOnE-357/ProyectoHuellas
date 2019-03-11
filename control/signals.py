from django.db.models.signals import post_save, pre_save
from datetime import datetime, date, time, timedelta
from django.dispatch import receiver
from django.contrib.auth.models import User
from persona.models import Persona, InfoComp, Fisico, Foto
from calzado.models import Calzado, FotoCalzado, Marca, Forma
from .models import Log

@receiver(post_save, sender=User)
def create_user(sender, instance, raw, created, **kwargs):
	u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
	dni=str(u.username) 
	nombre= str(u.first_name+" "+u.last_name)
	tabla=str(instance._meta.db_table)#Nombre de la tabla.
	objeto=int(instance.id)
	fecha=date.today()
	if created:
		accion="CREAR"	
	else:
		accion="ACTUALIZAR"
	Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)

@receiver(post_save, sender=Persona)
def create_user(sender, instance, raw, created, **kwargs):
	u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
	dni=str(u.username) 
	nombre= str(u.first_name+" "+u.last_name)
	tabla=str(instance._meta.db_table)#Nombre de la tabla.
	objeto=int(instance.id)
	fecha=date.today()
	if created:
		accion="CREAR"	
	else:
		accion="ACTUALIZAR"
	Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)

@receiver(post_save, sender=InfoComp)
def create_user(sender, instance, raw, created, **kwargs):
	u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
	dni=str(u.username) 
	nombre= str(u.first_name+" "+u.last_name)
	tabla=str(instance._meta.db_table)#Nombre de la tabla.
	objeto=int(instance.id)
	fecha=date.today()
	if created:
		accion="CREAR"	
	else:
		accion="ACTUALIZAR"
	Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)

@receiver(post_save, sender=Fisico)
def create_user(sender, instance, raw, created, **kwargs):
	u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
	dni=str(u.username) 
	nombre= str(u.first_name+" "+u.last_name)
	tabla=str(instance._meta.db_table)#Nombre de la tabla.
	objeto=int(instance.id)
	fecha=date.today()
	if created:
		accion="CREAR"	
	else:
		accion="ACTUALIZAR"
	Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)

@receiver(post_save, sender=Foto)
def create_user(sender, instance, raw, created, **kwargs):
	u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
	dni=str(u.username) 
	nombre= str(u.first_name+" "+u.last_name)
	tabla=str(instance._meta.db_table)#Nombre de la tabla.
	objeto=int(instance.id)
	fecha=date.today()
	if created:
		accion="CREAR"	
	else:
		accion="ACTUALIZAR"
	Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)

@receiver(post_save, sender=Calzado)
def create_user(sender, instance, raw, created, **kwargs):
	u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
	dni=str(u.username) 
	nombre= str(u.first_name+" "+u.last_name)
	tabla=str(instance._meta.db_table)#Nombre de la tabla.
	objeto=int(instance.id)
	fecha=date.today()
	if created:
		accion="CREAR"	
	else:
		accion="ACTUALIZAR"
	Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)

@receiver(post_save, sender=FotoCalzado)
def create_user(sender, instance, raw, created, **kwargs):
	u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
	dni=str(u.username) 
	nombre= str(u.first_name+" "+u.last_name)
	tabla=str(instance._meta.db_table)#Nombre de la tabla.
	objeto=int(instance.id)
	fecha=date.today()
	if created:
		accion="CREAR"	
	else:
		accion="ACTUALIZAR"
	Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)

@receiver(post_save, sender=Marca)
def create_user(sender, instance, raw, created, **kwargs):
	u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
	dni=str(u.username) 
	nombre= str(u.first_name+" "+u.last_name)
	tabla=str(instance._meta.db_table)#Nombre de la tabla.
	objeto=int(instance.id)
	fecha=date.today()
	if created:
		accion="CREAR"	
	else:
		accion="ACTUALIZAR"
	Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)

@receiver(post_save, sender=Forma)
def create_user(sender, instance, raw, created, **kwargs):
	u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
	dni=str(u.username) 
	nombre= str(u.first_name+" "+u.last_name)
	tabla=str(instance._meta.db_table)#Nombre de la tabla.
	objeto=int(instance.id)
	fecha=date.today()
	if created:
		accion="CREAR"	
	else:
		accion="ACTUALIZAR"
	Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)