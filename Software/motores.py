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

class Cangilon():

	def __init__(self, pin1, pin2, pwm):

		self.pin1= pin1
		self.pin2= pin2
		self.pwm= pwm

		gpio.setup(self.pin1, gpio.OUT)
		gpio.setup(self.pin2, gpio.OUT)

		PWM= gpio.PWM(self.pin2, 100)

	def girarD(self):

		PWM.stop()
		gpio.output(self.pin1, "True")
		PWM.start(self.pwm)

		return 0

	def girarI(self):

		PWM.stop()
		gpio.output(self.pin1, "False")
		PWM.start(self.pwm)

		return 0

	def detener(self):

		PWM.stop()
		gpio.output(self.pin1, "False")
		
		return 0

class Propulsion():

	def __init__(self, pin1, pin2, pwm):

		self.pin1= pin1
		self.pin2= pin2
		self.pwm= pwm

		gpio.setup(self.pin1, gpio.OUT)
		gpio.setup(self.pin2, gpio.OUT)

		PWM1= gpio.PWM(self.pin1, 100)
		PWM2= gpio.PWM(self.pin2, 100)

	def girarD(self):

		PWM1.stop()
		PWM2.start(self.pwm)

		return 0

	def girarI(self):

		PWM2.stop()
		PWM1.start(self.pwm)

		return 0

	def detener(self):

		PWM1.stop()
		PWM2.stop()
		
		return 0
