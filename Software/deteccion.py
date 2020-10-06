import sensoresUS as US 
import numpy as np 

def esquivarObstaculos():
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
			self.Lfd=medida[0] #Frontal derecho
			self.Lsd=medida[1] #Diagonal derecho
			self.Lld=medida[2] #Lateral derecho
			self.ltd=medida[3] #Atras derecho
			self.Lti=medida[4] #Atras izquierdo
			self.Lli=medida[5] #Lateral izquierdo
			self.Lsi=medida[6] #Diagonal izquierdo
			self.lfi=medida[7] #Frontal izquierdo

	med=mediciones()

	med.medicion()
	#-------------------------------------------------------Caso: el barco esta centrado al obstáculo---------------------------------------------------------
	if med.Lfi > 0 and med.Lfd > 0:
		#Estoy en el medio del obstáculo (Detectan los dos)
		#------------------------------------Tengo espacio para esquivar en ambos lados------------------------------------
		if med.Lli == 0 and med.Lld == 0:
			while med.Lli <= 300 or med.Lld <= 300:
				med.medicion()
				#Una vez que estoy a 3 metros empiezo a esquivar

			#Calculo la dirección deseada
			DD = DireccionDeseada(DATOS.lat, DATOS.long, waypoint)
			DA = DATOS.curso
			DeltaD = DD - DA

			if DeltaD < 0:
				#Si la dirección deseada es para la derecha: Giro para la derecha.
				timon.girar(30)
				while med.Lfi > 0:
					med.medicion()
					#Sigo girando hasta que el sensor Frontal Izquierdo ya no mida más
				timon.girar(-30)
				while med.Lsi <= 200:
					med.medicion()
					#Me vuelvo a enderezar con el curso deseado una vez que el sensor Diagonal Izquierdo mide más de 2m
				return 0

			if DeltaD > 0:
				#Si la dirección deseada es para la izquierda: Giro para la izquierda.
				timon.girar(-30)
				while med.Lfd > 0:
					med.medicion()
					#Sigo girando hasta que el sensor Frontal Derecho ya no mida más
				timon.girar(30)
				while med.Lsd <= 200:
					med.medicion()
					#Me vuelvo a enderezar con el curso deseado una vez que el sensor Diagonal Derecho mide más de 2m
				return 0
		#---------------------------------------------------------------------------------------------------------------

		#------------------------------------Tengo espacio para esquivar a la izquierda---------------------------------
		#Calculo el caso de que el lateral izquierdo no mida nada o que lo que mida sea mayor al lateral derecho
		if med.Lli == 0 and med.Lld > 0 or med.Lli > med.Lld:
			timon.girar(-30)
			while med.Lfd > 0:
				med.medicion()
				#Sigo girando hasta que el sensor Frontal Derecho ya no mida más
			timon.girar(30)
			while med.Lsd <= 200:
				med.medicion()
				#Me vuelvo a enderezar con el curso deseado una vez que el sensor Diagonal Derecho mide más de 2m
			return 0
		#---------------------------------------------------------------------------------------------------------------

		#-----------------------------------Tengo espacio para esquivar a la derecha------------------------------------
		#Calculo el caso de que el lateral derecho no mida nada o que lo que mida sea mayor al lateral izquierdo
		if med.Lld == 0 and med.Lli > 0 or med.Lld > med.Lli:
			timon.girar(30)
			while med.Lfi > 0:
				med.medicion()
				#Sigo girando hasta que el sensor Frontal Izquierdo ya no mida más
			timon.girar(-30)
			while med.Lsi <= 200:
				med.medicion()
				#Me vuelvo a enderezar con el curso deseado una vez que el sensor Diagonal Izquierdo mide más de 2m
			return 0
		#---------------------------------------------------------------------------------------------------------------

	#-------------------------------------------------FIN // Caso: el barco esta centrado al obstáculo---------------------------------------------------------

	#--------------------------------------------------Caso: el barco está a la derecha del obstáculo----------------------------------------------------------
	if med.Lfi > 0 and med.Lfd == 0:
		#Estoy a la derecha del obstáculo (Detecta el izquierdo)
		while med.Lfi >= 300:
			med.medicion()
			if med.Lfi == 0: #Si antes de llegar a los 3m dejo de detectar significa que puedo pasar bien sin esquivar
				return 0
		#Empiezo a esquivar a los 3 metros

		timon.girar(30)
		while med.Lfi > 0:
			med.medicion()
			#Sigo girando hasta que el sensor Frontal Izquierdo ya no mida más
		timon.girar(-30)
		while med.Lsi <= 200:
			med.medicion()
			#Me vuelvo a enderezar con el curso deseado una vez que el sensor Diagonal Izquierdo mide más de 2m
		return 0

	#----------------------------------------------FIN // Caso: el barco está a la derecha del obstáculo-------------------------------------------------------

	#------------------------------------------------Caso: el barco está a la izquierda del obstáculo----------------------------------------------------------
	if med.Lfd > 0 and med.Lfi == 0:
		#Estoy a la izquierda del obstáculo (Detecta el derecho)
		while med.Lfd >= 300:
			med.medicion()
			if med.Lfd == 0: #Si antes de llegar a los 3m dejo de detectar significa que puedo pasar bien sin esquivar
				return 0
		#Empiezo a esquivar a los 3 metros

		timon.girar(-30)
		while med.Lfd > 0:
			med.medicion()
			#Sigo girando hasta que el sensor Frontal Derecho ya no mida más
		timon.girar(30)
		while med.Lsd <= 200:
			med.medicion()
			#Me vuelvo a enderezar con el curso deseado una vez que el sensor Diagonal Derecho mide más de 2m
		return 0
		
	#---------------------------------------------FIN // Caso: el barco está a la izquierda del obstáculo------------------------------------------------------