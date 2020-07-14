import RPi.GPIO as GPIO
import time
import threading 
import pynmea2 as nmea
import numpy as np 
import motores as mt 
import math
from lib_nrf24 import NRF24
import spidev
import sensoresUS as US 

#estado del codigo= naranja

GPIO.setmode(GPIO.BCM)

#//////////////// defino la lista que va a guardar las variables/////////////
class Data():

	def __init__(self):

		self.lat=0
		self.long=0
		self.curso=0
		self.escan=0
		self.obstaculo=0

#//////////////// funciones de Piloto Automatico////////////////

def pilotoAutomatico():

#-----------------------------------------------------------------------------------------------------------

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
					pass

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
					pass
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
				pass
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
				pass
			#---------------------------------------------------------------------------------------------------------------

		#-------------------------------------------------FIN // Caso: el barco esta centrado al obstáculo---------------------------------------------------------

		#--------------------------------------------------Caso: el barco está a la derecha del obstáculo----------------------------------------------------------
		if med.Lfi > 0 and med.Lfd == 0:
			#Estoy a la derecha del obstáculo (Detecta el izquierdo)
			while med.Lfi >= 300:
				med.medicion()
				if med.Lfi == 0: #Si antes de llegar a los 3m dejo de detectar significa que puedo pasar bien sin esquivar
					pass
			#Empiezo a esquivar a los 3 metros

			timon.girar(30)
			while med.Lfi > 0:
				med.medicion()
				#Sigo girando hasta que el sensor Frontal Izquierdo ya no mida más
			timon.girar(-30)
			while med.Lsi <= 200:
				med.medicion()
				#Me vuelvo a enderezar con el curso deseado una vez que el sensor Diagonal Izquierdo mide más de 2m
			pass
		#----------------------------------------------FIN // Caso: el barco está a la derecha del obstáculo-------------------------------------------------------

		#------------------------------------------------Caso: el barco está a la izquierda del obstáculo----------------------------------------------------------
		if med.Lfd > 0 and med.Lfi == 0:
			#Estoy a la izquierda del obstáculo (Detecta el derecho)
			while med.Lfd >= 300:
				med.medicion()
				if med.Lfd == 0: #Si antes de llegar a los 3m dejo de detectar significa que puedo pasar bien sin esquivar
					pass
			#Empiezo a esquivar a los 3 metros

			timon.girar(-30)
			while med.Lfd > 0:
				med.medicion()
				#Sigo girando hasta que el sensor Frontal Derecho ya no mida más
			timon.girar(30)
			while med.Lsd <= 200:
				med.medicion()
				#Me vuelvo a enderezar con el curso deseado una vez que el sensor Diagonal Derecho mide más de 2m
			pass
		#---------------------------------------------FIN // Caso: el barco está a la izquierda del obstáculo------------------------------------------------------

	def girar(angulo):
		
		US.medicion()
		if (angulo<0):
			while(Lsi <= 250):
				US.medicion()

		if (angulo>0):
			while(Lsd <= 250):
				US.medicion()

		timon.girar(angulo)


	def distancia(lat1, lng1 , waypoint):
		lat2=waypoint[0, 0]
		lng2=waypoint[0, 1]
		r=6371000
		c=(math.pi)/180
		#Fórmula de haversine
		d = 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))
		return d

	def DireccionDeseada(lat1, lng1, waypoint):
		lat2=waypoint[0, 0]
		lng2=waypoint[0, 1]
		dlon=lng2-lng1 
		a1=sin(dlon)*cos(lat2)
		a2=(cos(lat1)*sin(lat2))-(sin(lat1)*cos(lat2)*cos(dlon))
		curso=atan2(a1, a2)

		if(curso < 0):
			curso += 2*math.pi

		return degrees(curso)

	def GirarAWP(waypoint):

		#primero hace un primer chequeo de la diferencia de direccion
		DD= DireccionDeseada(DATOS.lat, DATOS.long, waypoint)
		DA= DATOS.curso #Direccion actual dado por el modulo gps
		DeltaD= DD - DA

		#si no es demasiado no gira
		if (abs(DeltaD)<= 10):
			return 0

		#si es mucho lo corrige
		if (abs(DeltaD) >= 30):
			
			ang= round((DeltaD/abs(DeltaD)),0)*30
			girar(ang)

			while(abs(DeltaD) >= 30):
				DD= DireccionDeseada(DATOS.lat, DATOS.long, waypoint)
				DA= DATOS.curso
				DeltaD= DD - DA

		if (abs(DeltaD) <= 30):
			ang=round(DeltaD, 0)
			girar(ang)
			while(abs(DeltaD)<=30):
				DD= DireccionDeseada(DATOS.lat, DATOS.long, waypoint)
				DA= DATOS.curso
				DeltaD= DD - DA
				if ((ang - DeltaD) <= 1):
					pass
				else:
					girar(ang-DeltaD)
					ang=round(DeltaD, 0)
			
		return 0

	def LlegadaAlWP(destino):
		#comparar nuestra direccion con el destino
		dis= distancia(DATOS.lat, DATOS.long, destino)

		if(abs(dis) <= 5):
			return 0
		else:
			return 1

#---------------------------------------------------------------------------------------------------------------

	timon= mt.PaP(4, 17, 27, 22)
	Cangilon= mt.Cangilon(6, 13, 50)
	motorDirec= mt.Propulsion(18, 12, 50)

	#meto primera
	Cangilon.girarD()
	motorDirec.girarD()

	#en esta array se guardan los waypoints a recorrer 
	#cada waypoint se guarda en una fila distinta
	waypoints= np.empty((TotaldeWaypoints, 2))

	#se recorren todos los watpoints uno por uno
	for i in range (0, len(waypoints)):
		#la idea es que corrija el rumbo a lo largo del trayecto cada xx tiempo
		while(LlegadaAlWP(waypoints[i]) != 1):
			if DATOS.obstaculo == 1:
				esquivarObstaculos()
			GirarAWP(waypoints[i])
			time.sleep(5)

	Cangilon.detener()
	motorDirec.detener()
	
#//////////////// funciones de RF //////////////////////

def comRF():
	class slave():

	    def __init__(self, pin1, pin2):
	        self.pin1=pin1
	        self.pin2=pin2

	        #configuracion del modulo

	        pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

	        radio = NRF24(GPIO, spidev.SpiDev())

	        radio.begin(self.pin1, self.pin2)

	        radio.setRetries(15,15)
	        radio.setPayloadSize(32)
	        radio.setChannel(0x60)
	        radio.setDataRate(NRF24.BR_2MBPS)
	        radio.setPALevel(NRF24.PA_MIN)

	        radio.setAutoAck(True)
	        radio.enableDynamicPayloads()
	        radio.enableAckPayload()

	        radio.openReadingPipe(1, pipes[1])
	        radio.openWritingPipe(pipes[0])

	        radio.printDetails()

	        radio.startListening()

    #--------------------------------------------Funciones de sensores---------------------------------------------------
    #Abro el SPI
    spi = spidev.SpiDev()
    spi.open(0, 0)

    #Defino un canal para cada sensor
    sCorriente1 = 0
    sCorriente2 = 1
    sBateria = 2
    sMotDir = 3

    def tomarDatos(canal):
    	#Primero tomamos los datos crudos del conversor A/D
    	datosCrudos = spi.xfer([1, (8 + canal) << 4, 0])
    	#Proceso esta información para tenerla en un numero de 0 a 1023
    	datosProcesados = ((datosCrudos[1]&3) << 8) + datosCrudos[2]
    	return datosProcesados

	def bateria(redondeoDecimal = 3):
	    porcentajeB = tomarDatos(sBateria)
	    voltaje = (porcentajeB * 5) / float(1023)
	    voltaje = round(voltaje, redondeoDecimal)
	    if pocentajeB < 808:
	    	porcentaje = 0
	    else:
	    	porcentaje = (porcentajeB * 100) / float(1023)
	    	porcentaje = round(porcentaje)
	    return porcentaje

	def consPropulsion(redondeoDecimal = 3):
	    consumoB = tomarDatos(sCorriente1) #Tomo el valor en bits
	    voltaje = (consumoB * 5) / float(1023) #Lo convierto a cuando voltaje representa
	    voltaje = round(voltaje, redondeoDecimal) #Redondeo a dos decimales
	    consumo = (voltaje - 2.5) * 0.1 #Convierto el valor de voltaje en corriente (Relación: 100mV = 1A)
	    return consumo

	def consCangilon():
	    consumoB = tomarDatos(sCorriente2) #Tomo el valor en bits
	    voltaje = (consumoB * 5) / float(1023) #Lo convierto a cuando voltaje representa
	    voltaje = round(voltaje, redondeoDecimal) #Redondeo a dos decimales
	    consumo = (voltaje - 2.5) * 0.1 #Convierto el valor de voltaje en corriente (Relación: 100mV = 1A)
	    return consumo

	def anguloMotDir():
	    #Detecto si el motor de dirección falla
	    GPIO.setup(12, GPIO.IN)
	    return anguloMotDir

	def estacionamiento():
		#Detecto si el barco estaciona
		GPIO.setup(26, GPIO.IN)
		return estacionamiento

	def PS():
		#Detecto si el panel solar carga o no
		GPIO.setup(6, GPIO.IN)
		return PS
	#--------------------------------------------------------------------------------------------------------------------------

	#Función de recibir mensjaes
	def recibirRF():
	    rcvMsj = []
	    radio.read(rcvMsj, radio.getDynamicPayloadSize())
	    msj = ""
	    for n in rcvMsj:
	        if (n >= 32 and n <= 126)
	            msj += chr(n)
	    return msj

	#Función de enviar datos
	def enviarRF(msj):
		mensaje = list(msj)
		radio.Write(mensaje)

	#Recibo el comando de zarpar
	comando = recibirRF()
	if comando == "ZARPAR":
		TGPS = threading.Thread(name="GPS", target=GPS)
		TPA = threading.Thread(name="PA", target=pilotoAutomatico)
		TGPS.start()
		
		while True:
    			if(DATOS.escan==1):
        			break
	
		TPA.start()

		while True:
			lat = DATOS.lat
			lon = DATOS.long
			dirr = DATOS.curso
			enviarRF(lat)
			enviarRF(lon)
			enviarRF(dirr)
			prop = consPropulsion()
			enviarRF(prop)
			cang = consCangilon()
			enviarRF(cang)
			bat = bateria()
			enviarRF(bat)
			PS = PS()
			enviarRF(PS)
			estacionamiento = estacionamiento()
			#Si el barco estaciona, salgo del loop
			if estacionamiento == 1:
				enviarRF(estacionamiento)
				break
			if estacionamiento == 0:
				enviarRF(estacionamiento)


#//////////////// funciones de GPS //////////////////////

def GPS():

	def disponible():
            #funcion que detecte disponibilidad de datos
            port="/dev/ttyAMA0"
            ser=serial.Serial(port, baudrate=9600, timeout=0.5)
            dataout=pynmea2.NMEAStreamReader()
            data=ser.readline()

            if data[0:6] == "$GPRMC":
                datos=pynmea2.parse(newdata)
                while True:
                    if datos.status == A:
                        break

                DATOS.escan==1
            return 0
        
	def lectura():
	    port="/dev/ttyAMA0"
            ser=serial.Serial(port, baudrate=9600, timeout=0.5)
            dataout=pynmea2.NMEAStreamReader()
            data=ser.readline()

            if data[0:6] == "$GPRMC":
                pos=pynmea2.parse(newdata)
		DATOS.lat=pos.latitude
		DATOS.long=pos.longitude
		DATOS.curso=pos.direction

	    time.sleep(0.5)
	    return 0

        disponible()

        if (DATOS.escan==1):
            while True:
                lectura()
                
#////////////// inicio los hilos ////////////////////

DATOS= Data()

TRF = threading.Thread(name="RF", target=comRF)

RF.start()