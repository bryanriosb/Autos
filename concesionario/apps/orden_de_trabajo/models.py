# -*- encoding: utf-8 -*-

from django.db import models
from apps.empleado.models import Empleado
from apps.cliente.models import Cliente

#Estados de la reparacion del vehiculo

#El vehiculo esta en el taller, pero no se ha revisado
PENDIENTE = 'Pendiente'
#El vehiculo esta en observacion
EN_OBSERVACION = 'En observacion'
#El vehiculo esta en reparacion
EN_REPARACION = 'En reparacion'
#El vehiculo ya esta reparado
FINALIZADO = 'Finalizado'

tipo_choice = (
	(PENDIENTE, 'Pendiente'),
	(EN_OBSERVACION, 'En observacion'),
	(EN_REPARACION, 'En reparacion'),
	(FINALIZADO, 'Finalizado'),
 )

class OrdenDeTrabajo(models.Model):
	"""Define la organizacion del los datos de una orden de trabajo en la base de datos."""

	#Django por defecto, cuando los modelos no tienen primary_key, coloca una llamada "id"

	#Empleado que realiza la orden de trabajo, relacion uno a muchos 
	empleado = models.ForeignKey(Empleado)
	#dueno del auto que entra al taller, relacion uno a muchos 
	cliente = models.ForeignKey(Cliente)
	#placa del vehiculo que entra al taller 
	placa = models.CharField(null=True,blank=True,max_length=7)
	#Fecha de entrada al taller
	fecha_entrada = models.DateField(blank=True, null=True)
	#Fecha de salida del taller
	fecha_salida = models.DateField(blank=True, null=True)
	#Descripcion del problema que presenta el vehiculo. Dada por el cliente 
	descripcion = models.CharField(null=True,blank=True,max_length=50)
	#Estado del vehiculo en el taller
	estado_reparacion = models.CharField(null=True,blank=True,max_length=50,choices=tipo_choice,default=PENDIENTE)
	#Observacion de los daños del vehiculo
	observacion = models.TextField(null=True,blank=True,max_length=200)
	#Estado de la OrdenDeTrabajo, Activa/inactiva
	habilitado = models.BooleanField(default = True)
	
	#Permite hacer modificaciones agregadas a la representacion del modelo 
	class Meta:
		ordering = ['fecha_entrada']
		verbose_name_plural = "ordendetrabajo"

	#Permite determinar una representacion en string del objeto repuesto
	def __str__(self):
		return self.fecha_entrada

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.fecha_entrada 






