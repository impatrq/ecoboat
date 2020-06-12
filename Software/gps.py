import pynmea2 as nmea
import serial
import numpy

def lectura(self):
	port="/dev/ttyAMA0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout=pynmea2.NMEAStreamReader()
	data=ser.readline()

	if data[0:6] == "$GPRMC":
		datos=pynmea2.parse(newdata)
		lat=datos.latitude
		lng=datos.longitude
		cur=datos.direction

	return 0

	