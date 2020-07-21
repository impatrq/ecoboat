import RPi.GPIO as GPIO
import time
import threading 
import pynmea2 as nmea
import numpy as np 
import motores as mt

datos= [0,0,0,0]
#0 = latitud
#1 = longitud
#2 = curso
#3 = fin de escaneo

def PilotoAutomatico():

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

    def Girar(waypoint):

        #primero hace un primer chequeo de la diferencia de direccion
        DD= DireccionDeseada(DATOS.lat, DATOS.long, waypoint)
        DA= DATOS.curso #Direccion actual dado por el modulo gps
        DeltaD= DD - DA

        #si no es demasiado no gira
        if (abs(DeltaD)<= 10):
            return 0

        #si es mucho lo corrige
        #Si el ángulo que tiene que girar es mayor a 30, gira al máximo.
        if (abs(DeltaD) >= 30):
            
            ang= round((DeltaD/abs(DeltaD)),0)*30
            timon.girar(ang)

            while(abs(DeltaD) >= 30): #Sigue al máximo hasta que DeltaD sea 30°
                DD= DireccionDeseada(DATOS.lat, DATOS.long, waypoint)
                DA= DATOS.curso
                DeltaD= DD - DA

        #Si el ángulo que tiene que girar es menor a 30 gira menos.
        if (abs(DeltaD) <= 30):
            ang=round(DeltaD, 0) #Redondeo el ángulo de giro
            timon.girar(ang) #Giro el timón la misma cantidad de grados que la DeltaD
            while(abs(DeltaD)<=30):
                DD= DireccionDeseada(DATOS.lat, DATOS.long, waypoint)
                DA= DATOS.curso
                DeltaD= DD - DA
                if ((ang - DeltaD) <= 1): #Si DeltaD es 1° dejo de girar
                    pass
                else:
                    timon.girar(ang-DeltaD) #Voy corrigiendo el giro a medida que DeltaD va disminuyendo
                    ang=round(DeltaD, 0)
            
        return 0

    def LlegadaAlWP(destino):
            
        #comparar nuestra direccion con el destino
        dis= distancia(datos[0], datos[1], destino)
                    
        if(abs(dis) <= 5):
            return 0
        else:
            return 1

    timon= mt.PaP(4, 17, 27, 22)
    motorDirec= mt.puenteH(18, 12, 50)
    #meto primera
    motorDirec.girarD()

    #en esta array se guardan los waypoints a recorrer 
    #cada waypoint se guarda en una fila distinta
    waypoints= np.empty((TotaldeWaypoints, 2))

    #se recorren todos los watpoints uno por uno
    for i in range (0, len(waypoints)):
	#la idea es que corrija el rumbo a lo largo del trayecto cada xx tiempo
		while(LlegadaAlWP(waypoints[i]) != 1):
			Girar(waypoints[i])
	        	time.sleep(5)


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

                datos[3]==1
            return 0
        
	def lectura():
	    port="/dev/ttyAMA0"
            ser=serial.Serial(port, baudrate=9600, timeout=0.5)
            dataout=pynmea2.NMEAStreamReader()
            data=ser.readline()

            if data[0:6] == "$GPRMC":
                pos=pynmea2.parse(newdata)
		datos[0]=pos.latitude
		datos[1]=pos.longitude
		datos[2]=pos.direction

	    time.sleep(0.05)
	    return 0

        disponible()

        if (datos[3]==1):
            while True:
                lectura()
                time.sleep(1)

gps= threading.Thread(target=GPS)
PA= threading.Thread(target=PilotoAutomatico)

gps.start()

while True:
    if(datos[3]==1):
        break

PA.start()
    


