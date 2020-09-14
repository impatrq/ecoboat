import pynmea2 as nmea
import serial
import numpy

def lectura(self):
	while True:
		port="/dev/ttyAMA0"
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)
		dataout=pynmea2.NMEAStreamReader()
		data=ser.readline()

		if data[0:6] == b'$GPRMC':
		    data = data.decode("utf-8","ignore")
		    datos=pynmea2.parse(data)
		    lat=datos.latitude
		    lng=datos.longitude
		    cur=datos.true_course
		    DATOS.lat = lat
		    DATOS.long = lng
		    DATOS.curso = cur

	return 0