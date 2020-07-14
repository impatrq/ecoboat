import sensoresUS as US 
import numpy as np 

#despues hay que poner este codigo como un hilo en el programa principal
#estado del codigo = verde
class mediciones():

	def __init__(self):
		self.Lfi=0
		self.Lfd=0
		self.Lsi=0
		self.Lsd=0
		self.Lli=0
		self.Lld=0
		self.Lti=0
		self.Ltd=0

	def medicion(self):
		medida=US.lectura()
		self.Lfd=medida[0]
		self.Lsd=medida[1]
		self.Lld=medida[2]
		self.ltd=medida[3]
		self.Lti=medida[4]
		self.Lli=medida[5]
		self.Lsi=medida[6]
		self.lfi=medida[7]

med=mediciones()

while True:
	med.medicion()
	#-------------------------------------------------------Caso: el barco esta centrado al obstáculo----------------------------------------------------------
	if med.Lfi <= 400 and med.Lfd <= 400:
		#Estoy en el medio del obstáculo (Detectan los dos)
		if med.Lli == 0 and med.Lld == 0:
			while med.Lli <= 300 or med.Lld <= 300:
				med.medicion()
				#Una vez que estoy a 3 metros empiezo a esquivar
				#Si tiene espacio en los dos lados gira para el más cercano a la dirección deseada
			if DeltaD < 0:
				#Si la dirección deseada es para la derecha: Giro para la derecha.
				timo.girar(30)
				while med.Lfi > 0:
					med.medicion()
				timon.girar(-30)

			if DeltaD > 0:
				giro = 1

		if med.Lli < med.Lld:
			#Si hay mas espacio a la derecha voy por ese lado
			giro = 1
		while True:

	if med.Lfi <= 400:
		#Estoy a la derecha del obstáculo (Detecta el izquierdo)

	if med.Lfd <= 400:
		#Estoy a la izquierda del obstáculo (Detecta el derecho)


	while(med.Lfi <=400 and med.Lfd > 400):
		med.medicion()
		#reviso el lobulo secundario
		if (med.Lsd > 400):
			#doblar hacia la derecha
		else if(med.Lsi > 400):
			#si no se puede doblar a la derecha
			#doblar hacia la izquierda de forma mas cerrada

	while(med.Lfd <=400 and med.Lfi > 400):
		med.medicion()
		#reviso el labulo secundario
		if (med.Lsi > 400):
			#doblar hacia la izquierda
		else if(med.Lsd > 400):
			#si no se puede doblar a la izquierda
			#doblar hacia la derecha de forma mas cerrada

	while(med.Lfd <=400 and med.Lfi <=400):
		
			#revisar los sensores secundarios y laterales
