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
