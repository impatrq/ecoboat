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

#Defino el modo de uso de los pines GPIO
GPIO.setmode(GPIO.BCM)

#---------------------Variable global-----------------------
class Data():

	def __init__(self):
		self.lat=0
		self.long=0
		self.curso=0
		self.escan=0

DATOS= Data()
#-----------------------------------------------------------

#--------------------------------------------------------------------GPS-----------------------------------------------------------------------
def GPS():

	def disponible():
        #Función que detecta disponibilidad de datos
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

	while escan = 0:
    	disponible()

    while True:
    	lectura()                
#-------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------Piloto automático-------------------------------------------------------------
def pilotoAutomático():
	#------------------------Medición de los sensores ultrasónicos---------------
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
				self.Ltd=medida[3] #Atras derecho
				self.Lti=medida[4] #Atras izquierdo
				self.Lli=medida[5] #Lateral izquierdo
				self.Lsi=medida[6] #Diagonal izquierdo
				self.Lfi=medida[7] #Frontal izquierdo
				
	med = mediciones()
	#---------------------------------------------------------------------------

	#---------------------------------------------Funciones de navegación---------------------------------------------
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

	def LlegadaAlWP(destino):
		#comparar nuestra direccion con el destino
		dis= distancia(DATOS.lat, DATOS.long, destino)

		if(abs(dis) <= 5):
			return 0
		else:
			return 1
	#------------------------------------------------------------------------------------------------------------------

	#--------------------------------------------------Red Neuronal----------------------------------------------------
	def redNeuronal():
		#Código de la red neuronal.
	#------------------------------------------------------------------------------------------------------------------

	#---------------------------------------------------Control PID----------------------------------------------------
	def controlPID(waypoint):
		KP = 1 #Constante Proporcional
		KI = 0.1 #Constante Integral
		KD = 0.2 #Constante Derivativa
		ZI = 5 #Zona activa de la Integral
		#Defino el thread de la red neuronal
		TRN = threading.Thread(name = redNeuronal, target = redNeuronal)

		while DeltaD >= 0.005 or DeltaD <= -0.005: #Le pusimos que funcione hasta un error un poco mayor a 0 debido a el margen de error del GPS
			med.medicion()		#Si se detecta un obstáculo mientras giro voy a la RN
			if Lli <= 150 or Lsi <= 150 or Lfi <= 100 or Lld <= 150 or Lsd <= 150 or Lfd <= 100:
				TNR.start()
				TNR.join()
			#Primero calculo el error
			DD= DireccionDeseada(DATOS.lat, DATOS.long, waypoint)
			DA= DATOS.curso #Direccion actual dado por el modulo gps
			DeltaD= DD - DA
			
			if DeltaD <= ZI and (DeltaD >= 0.005 or DeltaD <= -0.005):
				#Si estamos en la zona activa de la integral empezamos a sumar ángulo
				errorT += DeltaD
			else:
				#Si estamos fuera de la zona activa de la integral, asignamos un 0 a la integral
				errorT = 0

			if errorT >= 50/KI:
				#Le ponemos un límite a la integral
				errorT = 50/KI

			Proporcional = DeltaD * KP
			Integral = errorT * KI
			Derivativa = (DeltaD - UltimoError) * KD

			UltimoError = DeltaD #Guardo el último error

			#Obtengo el valor del ángulo para el timón
			angulo = Proporcional + Integral + Derivativa

			if abs(angulo) >= 30 and DeltaD > 0: #Caso: DeltaD positivo
				#Si el ángulo es mayor que el máximo de giro del timón giro 30°
				angulo = 30

			if abs(angulo) >= 30 and DeltaD < 0: #Caso: DeltaD negativo
				#Si el ángulo es mayor que el máximo de giro del timón giro 30°
				angulo = -30

			return angulo
	#------------------------------------------------------------------------------------------------------------------

	#--------------------------------------------Inicio el piloto automático-------------------------------------------
	#Creo objetos para los motores
	timon= mt.PaP(4, 17, 27, 22)
	Cangilon= mt.Cangilon(6, 13, 50)			#Con un 1 en el pin de selección giramos horario, con un 0 antihorario.
	motorDirec= mt.Propulsion(18, 12, 50)		#Con el 12 giro horario y con el 18 antihorario.

	#Meto primera
	Cangilon.girarD()
	motorDirec.girarD()

	#En esta array se guardan los waypoints a recorrer 
	#Cada waypoint se guarda en una fila distinta
	waypoints= np.empty((TotaldeWaypoints, 2))

	#Se recorren todos los watpoints uno por uno
	for i in range (0, len(waypoints)):
		#La idea es que corrija el rumbo a lo largo del trayecto cada xx tiempo
		while(LlegadaAlWP(waypoints[i]) != 1):
			controlPID(waypoints[i])	#Inicio el control PID que no va a hacer nada a no ser que el curso no sea el deseado

			med.medicion()		#Mido con todos los ultrasónicos
			if (Lsi > 0 and Lsi <= 400) or (Lfi > 0 and Lfi <= 400) or (Lsd > 0 and Lsd <= 400) or (Lfd > 0 and Lfd <= 400):
				#Si alguno de los ultrasónicos de adelante detecta algo entro en la RN
				redNeuronal()
			time.sleep(1)

	Cangilon.detener()
	motorDirec.detener()
#-------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------Módulos RF-------------------------------------------------------------------
def módulosRF():
	#Código de los módulos RF
#-------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------Inicio el programa--------------------------------------------------------------
TRF = threading.Thread(name="RF", target=comRF)

while True:
	RF.start()