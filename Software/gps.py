import pynmea2 as nmea
import serial
import math
import numpy

class Gps():

	def __init__(self):
		self.lat=0
		self.lng=0
		self.cur=0

		#falta algun while donde se quede esperando a que haya datos validos

	def lectura(self):
		port="/dev/ttyAMA0"
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)
		dataout=pynmea2.NMEAStreamReader()
		data=ser.readline()

		if data[0:6] == "$GPRMC":
			datos=pynmea2.parse(newdata)
			self.lat=datos.latitude
			self.lng=datos.longitude
			self.cur=datos.direction

		return 0

def distancia(gps, waypoint):
	gps.lectura()
	lat1=gps.lat
	lng1=gps.lng
	lat2=waypoint[0, 0]
	lng2=waypoint[0, 1]
	r=6371000
	c=(math.pi)/180
	#Fórmula de haversine
	d = 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))
	return d

