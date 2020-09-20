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
class Data():	#Aca guardamos todos los datos que van a ser utilizados por más de un hilo

	def __init__(self):
		self.lat=0		#Latitud
		self.long=0		#Longitud
		self.curso=0	#Curso
		self.escan=0	#Esta variable sirve para saber si el GPS recibe datos
		self.fin=0		#Esta variable es para detectar cuando el barco finaliza su recorrio
		self.timon=0	#Ángulo del timón, se utiliza para controlar el motor paso a paso
		self.bateria=0  #Porcentaje de batería
		self.motProp=0  #Consumo del motor de propulsión
		self.motCang=0  #Consumo del motor de la cinta transportadora

DATOS= Data()
#-----------------------------------------------------------

#--------------------------------------------------------------------GPS-----------------------------------------------------------------------
def GPS():

	def disponible():
        #Función que detecta disponibilidad de datos
        port="/dev/ttyAMA0"		#Puerto UART de la Raspberry
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)	#Inicio el puerto serial
		#Mido posición con el GPS
		dataout=pynmea2.NMEAStreamReader()
		data=ser.readline()
		#Tomo únicamente la línea que nos interesa que posee la posición
        if data[0:6] == b'$GPRMC':
		    data = data.decode("utf-8","ignore")
		    datos=pynmea2.parse(data)
		    DATOS.lat = datos.latitude
		    DATOS.long = datos.longitude
		    DATOS.curso = datos.true_course

		    DATOS.escan = 1
		    break
        return 0
        
	def lectura(self):	#----------------Función que toma los datos de posición-------------------
		port="/dev/ttyAMA0"		#Puerto UART de la Raspberry
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)	#Inicio el puerto serial
		
		while True:
			#Mido posición con el GPS
			dataout=pynmea2.NMEAStreamReader()
			data=ser.readline()

			#Tomo únicamente la línea que nos interesa que posee la posición
			if data[0:6] == b'$GPRMC':
			    data = data.decode("utf-8","ignore")
			    datos=pynmea2.parse(data)
			    DATOS.lat = datos.latitude
			    DATOS.long = datos.longitude
			    DATOS.curso = datos.true_course

			#Si el barco finalizó el recorrido, salimos del while
			if DATOS.fin = 1:
				break


	while DATOS.escan != 1:
		disponible()	#Una vez que detecto disponibilidad de datos inicio la lectura de datos e inicio los otros
						#hilos

    lectura()                
#-------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------Conversor Analógico/Digital--------------------------------------------------------
def conversor():

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
	#Esta función se utilzia para medir la distancia entre la ubicación actual y el próximo waypoint
	def distancia(lat1, lng1 , waypoint):	#lat1 y lng1 son los datos de posición actual
		lat2=waypoint[0, 0]
		lng2=waypoint[0, 1]
		r=6371000
		c=(math.pi)/180
		#Fórmula de haversine
		a = sin(c*(lat2-lat1)/2)**2
		b = cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2
		d = 2*r*asin(sqrt(a + b))
		return d

	#Esta función nos otorga el curso deseado
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

	#Est afunción nos indica cuando llegamos al waypoint
	def LlegadaAlWP(destino):
		#comparar nuestra direccion con el destino
		dis= distancia(DATOS.lat, DATOS.long, destino)

		if(abs(dis) <= 2):	#Detectamos que llegamos al wp una vez que estamos a menos de 2 metros (por los errores del GPS)
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

	#Comienzo a girar los motores de propulsión y de la cinta trtansportadora
	Cangilon.girarD()
	motorDirec.girarD()

	#En esta array se guardan los waypoints a recorrer 
	#Cada waypoint se guarda en una fila distinta
	waypoints= np.empty(([lat1, lng1], [lat2, lng2], ..., [latn, lngn]))

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
	#-----------------------------Funciones de enviar y recibir-----------------------------
	def enviar(dato):
	    datoStr = str(dato) #Convierto el dato en string
	    datoSend = list(datoStr) #Lo separo en letras
	    radio.Write(datoSend) #Lo envio

	def recibir():
	    #Guardo el mensjae en una variable
	    msjRecibido = []
	    radio.read(msjRecibido, radio.getDynamicPayloadSize())

	    #Decodifico el mensaje
	    mensaje = ""
	    for n in msjRecibido
	        if (n >= 32 and n <= 126)
	            mensaje += chr(n)
	    return mensaje
	#----------------------------------------------------------------------------------------

	#-------------------------------Configuración del NRF24l01-------------------------------
	#Estas son las direcciones que les asignamos a las direcciones de lectura y escritura
	pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

	radio = NRF24(GPIO, spidev.SpiDev())	#Creamos el objeto de la radio

    radio.begin(0, 7)	#Iniciamos la radio

    radio.setRetries(15,15)		#Cantidad de intentos
    radio.setPayloadSize(32)	#Tamaño máximo de los mensajes
    radio.setChannel(0x60)		#Canal de comunicación
    radio.setDataRate(NRF24.BR_2MBPS)	#Velocidad de transferencia
    radio.setPALevel(NRF24.PA_MAX)		#Consumo del módulo, esto define el alcance

    #Estas funcioines sirven para que el módulo sepa si se recibió el mensaje que envió
    radio.setAutoAck(True)
    radio.enableDynamicPayloads()
    radio.enableAckPayload()

    #Abro las direcciones
    radio.openReadingPipe(1, pipes[1])
    radio.openWritingPipe(pipes[0])

    radio.startListening()
    #-----------------------------------------------------------------------------------------

    #Se queda esperando un mensaje
    while not radio.available(0):
        time.sleep(1/100)

    #Cuando detecta un mensaje, lo guardo en una variable
    comando = recibir()

	#-----------------------------------Comando: ZARPAR---------------------------------------
	if comando == MSJZARPAR:	#Cuando recibo la orden de zarapar tengo que inicar los otros hilos
		TGPS = threading.Thread(name="GPS", target=GPS)		#Creo el hilo del GPS
		TPA = threading.Thread(name="PA", target=pilotoAutomatico)	#Creo el hilo del piloto automático
		#Inicio el GPS
		TGPS.start()
		
		while True:		#Espero a que el GPS reciba datos
    		if(DATOS.escan==1):
        		break
		#Inicio el Piloto Automático
		TPA.start()

		#Envió información a la interfaz de usuario
		while True:
			enviarRF(DATOS.lat)
			enviarRF(DATOS.lon)
			enviarRF(DATOS.curso)
			enviarRF(DATOS.motProp)
			enviarRF(DATOS.motCang)
			enviarRF(DATOS.bateria)
			#Si el barco finalizó el recorrido, dejo de enviar datos
			if DATOS.fin == 1:
				break
	#---------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------Inicio el programa--------------------------------------------------------------
#Creo el hilo del módulo RF
TRF = threading.Thread(name="RF", target=comRF)

#Inicio un bucle para que cuando el programa finalice, siga esperando a recibir orden de salir de vuelta.
while True:
	TRF.start()