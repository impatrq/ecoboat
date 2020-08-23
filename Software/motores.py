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

		#Defino los pines como salida
		gpio.setup(self.pin1, gpio.OUT)
		gpio.setup(self.pin2, gpio.OUT)
		gpio.setup(self.pin3, gpio.OUT)
		gpio.setup(self.pin4, gpio.OUT)

	def girar(self, grados): #Funcion para girar el timón

		if (grados<0):	#Cuando tiene que girar en sentido anti horario
			i=grados*512	#Este valor de 512 es por la reducción que tiene el motor
			for t in range (0, abs(i)):
				for e in range (0,4):	#Activo todos los estados para ir girando el motor hasta lleagr al valor deseado
					
					if estados[e, 0] == "True":
						gpio.output(self.pin1, estados[e, 1])
					else:
						gpio.output(self.pin1, estados[e, 0])

					if estados[e, 1] == "True":
						gpio.output(self.pin2, estados[e, 1])
					else:
						gpio.output(self.pin2, estados[e, 0])

					if estados[e, 2] == "True":
						gpio.output(self.pin3, estados[e, 1])
					else:
						gpio.output(self.pin3, estados[e, 0])
					
					if estados[e, 3] == "True":
						gpio.output(self.pin4, estados[e, 1])
					else:
						gpio.output(self.pin4, estados[e, 0])

					time.sleep(0.005)

			self.detener()

			return 0

		if (grados>=0):	#Cuando tiene que girar en sentido horario
			i=grados*512
			for t in range (0, i):
				for e in range (0,4):

					if estados[e, 3] == "True":
						gpio.output(self.pin1, estados[e, 1])
					else:
						gpio.output(self.pin1, estados[e, 0])

					if estados[e, 2] == "True":
						gpio.output(self.pin2, estados[e, 1])
					else:
						gpio.output(self.pin2, estados[e, 0])

					if estados[e, 1] == "True":
						gpio.output(self.pin3, estados[e, 1])
					else:
						gpio.output(self.pin3, estados[e, 0])
					
					if estados[e, 0] == "True":
						gpio.output(self.pin4, estados[e, 1])
					else:
						gpio.output(self.pin4, estados[e, 0])

					time.sleep(0.005)

			self.detener()

			return 0

	def detener(self):

		gpio.output(self.pin1, 0)
		gpio.output(self.pin2, 0)
		gpio.output(self.pin3, 0)
		gpio.output(self.pin4, 0)
		
		return 0

class Cangilon():

	def __init__(self, pin1, pin2, pwm):

		self.pin1= pin1	#Pin de selección de sentido de giro
		self.pin2= pin2	#Pin PWM
		self.pwm= pwm   #porcentaje de encendido del pwm

		gpio.setup(self.pin1, gpio.OUT)
		self.PWM= gpio.PWM(self.pin2, pwm)

	def girarD(self):

		self.PWM.stop()		#Paro el PWM
		gpio.output(self.pin1, 1)		#Cambio el sentido de giro. Con el pin en TRUE el giro es horario
		self.PWM.start(self.pwm)		#Inicio nuevamente el PWM

		return 0

	def girarI(self):

		self.PWM.stop()		#Paro el PWM
		gpio.output(self.pin1, 0)		#Cambio el sentido de giro. Con el pin en FALSE el giro es antihorario
		self.PWM.start(self.pwm)		#Inicio nuevamente el PWM

		return 0

	def detener(self):

		self.PWM.stop()
		gpio.output(self.pin1, 0)
		
		return 0

class Propulsion():

	def __init__(self, pin1, pin2, pwm):

		#Inicio los pines y los defino como PWM
		self.pin1= pin1
		self.pin2= pin2
		self.pwm= pwm

		gpio.setup(self.pin1, gpio.OUT)
		gpio.setup(self.pin2, gpio.OUT)

		self.PWM1= gpio.PWM(self.pin1, pwm)
		self.PWM2= gpio.PWM(self.pin2, pwm)

	def girarD(self):	#Giro horario

		self.PWM1.stop()
		self.PWM2.start(self.pwm)

		return 0

	def girarI(self):	#Giro antihorario

		self.PWM2.stop()
		self.PWM1.start(self.pwm)

		return 0

	def detener(self):

		self.PWM1.stop()
		self.PWM2.stop()
		
		return 0
