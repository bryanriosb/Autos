# -*- encoding: utf-8 -*-

from django.db import models
from apps.empleado.models import Empleado
from apps.cliente.models import Cliente

#Define la organizacion del los datos de una orden de trabajo en la base de datos
class OrdenDeTrabajo(models.Model):
#Django por defecto, cuando los modelos no tienen primary_key, coloca una llamada "id"

	#Empleado que realiza la orden de trabajo, relacion uno a muchos 
	empleado= models.ForeignKey(Empleado)
 
	#dueno del auto que entra al taller, relacion uno a muchos 
	cliente= models.ForeignKey(Cliente)

	#placa del vehiculo que entra al taller 
	placa= models.CharField(null=True,blank=True,max_length=6)

	#Fecha de entrada al taller
	fecha_entrada=models.DateField(blank=True, null=True)

	#Fecha de salida del taller
	fecha_salida=models.DateField(blank=True, null=True)

	#Descripcion del procedimiento realizado en el taller
	descripcion = models.CharField(null=True,blank=True,max_length=50)

	#estado del vehiculo
	estado_reparacion=models.CharField(null=True,blank=True,max_length=50)


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





