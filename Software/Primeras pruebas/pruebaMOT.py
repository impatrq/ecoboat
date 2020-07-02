import RPi.GPIO as gpio 
import time 
import numpy as np 

#agregar configuracion de pines gpio

estados=np.array([
	["True","False","False","False"],
	["False","True","False","False"],
	["False","False","True","False"],
	["False","False","False","True"],
	])

class PaP():

	def __init__(self, pin1, pin2, pin3, pin4):

		self.pin1= pin1
		self.pin2= pin2
		self.pin3= pin3
		self.pin4= pin4

		gpio.setup(self.pin1, gpio.OUT)
		gpio.setup(self.pin2, gpio.OUT)
		gpio.setup(self.pin3, gpio.OUT)
		gpio.setup(self.pin4, gpio.OUT)

	def girarH(self, grados):
		i=grados*512
		for t in range (0, i):
			for e in range (0,4):
				gpio.output(self.pin1, estados[e, 0])
				gpio.output(self.pin2, estados[e, 1])
				gpio.output(self.pin3, estados[e, 2])
				gpio.output(self.pin4, estados[e, 3])
				time.sleep(0.005)

		return 0

	def girarAH(self, grados):
		i=grados*512
		for t in range (0, i):
			for e in range (0,4):
				gpio.output(self.pin1, estados[e, 3])
				gpio.output(self.pin2, estados[e, 2])
				gpio.output(self.pin3, estados[e, 1])
				gpio.output(self.pin4, estados[e, 0])
				time.sleep(0.005)
			t+=1

		return 0

class puenteH():

	def __init__(self, pin1, pin2):

		self.pin1= pin1
		self.pin2= pin2

		gpio.setup(self.pin1, gpio.OUT)
		gpio.setup(self.pin2, gpio.OUT)

	def girarD(self):

		gpio.output(self.pin2, "False")
		gpio.output(self.pin1, "True")
		
		return 0

	def girarI(self):

		gpio.output(self.pin1, "False")
		gpio.output(self.pin2, "True")

		return 0

	def detener(self):

		gpio.output(self.pin1, "False")
		gpio.output(self.pin2, "False")

		return 0

timon=PaP(1,2,3,4)
prop=puenteH(5,6)

gpio.setup(7, gpio.IN)
gpio.setup(8, gpio.IN)
gpio.setup(9, gpio.IN)
gpio.setup(10, gpio.IN)

if (gpio.input(7)==True):
    timon.girarH()

if (gpio.input(8)==True):
    timon.girarAH()

if (gpio.input(9)==True):
    prop.girarD()

if (gpio.input(10)==True):
    prop.girarI()

if (gpio.input(9)==False && gpio.input(10)==False):
    prop.detener()
