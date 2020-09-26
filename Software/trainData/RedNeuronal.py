import numpy as np 
import math 
from random import randint, random
from time import sleep
import json

#funciones de activacion

def sigmoid(matrix):

	s=np.shape(matrix)

	if len(s)==2:
		for i in range(s[0]):
			for j in range(s[1]):
				matrix[i,j]= 1/(1+math.exp(-matrix[i,j]))
		return matrix
	else:
		for i in range(s[0]):
			matrix[i]= 1/(1+math.exp(-matrix[i]))
		return matrix

def TanH(matrix):
	for i in range(len(matrix)):
		a=math.exp(matrix[i])
		b=np.exp(-matrix[i])
		matrix[i]= (a-b)/(a+b)
	return matrix

#funciones de matriz

def mutarMatiz(matrix, rate):

	s=np.shape(matrix)

	for i in range(s[0]):
		for j in range(s[1]):

			if len(s)==2:
				prob= random()
				if prob > rate:
					matrix[i,j]=random()
				else:
					pass

			else:
				for h in range(s[2]):
					prob= random()
					if prob > rate:
						matrix[i,j,h]=random()
					else:
						pass
	
	return matrix

#Red neuronal

class RedNeuronal():

	def __init__(self, capas):

		self.capas=capas

		#iniciar los pesos de forma aleatoria
		#primera capa de la red
		self.biasE=np.random.random((capas[2],1))
		self.pesosE=np.random.random((capas[2], capas[0]))		

		#capas intermedias
		self.biasI=np.random.random((capas[2],capas[1]))
		self.pesosI=np.random.random((capas[2], capas[2], capas[1]-1))
		self.valoresI=np.empty((capas[2], capas[1]), dtype=float)

		#ultima capa de la red
		self.biasS=np.random.random((capas[3],1))
		self.pesosS=np.random.random((capas[3], capas[2])) 

	def mutar(self, rate):
		mutarMatiz(self.biasE ,rate)
		mutarMatiz(self.biasI ,rate)
		mutarMatiz(self.biasS ,rate)
		mutarMatiz(self.pesosE ,rate)
		mutarMatiz(self.pesosI ,rate)
		mutarMatiz(self.pesosS ,rate)
		
		return 0

	def resultado(self, inputs):

		inputs=inputs.astype(np.float)
		inputs=inputs.reshape(self.capas[0],1)
		#pesos de capas intermedias
		a=sigmoid(np.dot(self.pesosE, inputs)+self.biasE)
		self.valoresI[:,0]=a[:,0]

		if self.capas[1]>1:
			for i in range(self.capas[1]-1):
				a=sigmoid(np.dot(self.pesosI[:,:,i], self.valoresI[:,i])+self.biasI[:,i])
				self.valoresI[:, i+1]=a
				
			
		#ultima capa
		valoresIO= self.valoresI[:,self.capas[1]-1]
		outputs=sigmoid(np.dot(self.pesosS, valoresIO.reshape(len(valoresIO),1))+self.biasS)
		return outputs

	def entrenarES(self, inputs, respuestas):
	
		outputs= self.resultado(inputs)
		respuestas=respuestas.astype(np.float)

		lr=0.1

		#caculo los errores de todos las capas
		errS= respuestas-outputs.transpose()

		if self.capas[1]==1:
			errI=np.dot(self.pesosS.transpose(), errS.transpose())

		else:
			errI=np.empty((self.capas[2],self.capas[1]))
			a=np.dot(self.pesosS.transpose(), errS.transpose())
			errI[:, self.capas[1]-1]=a[:,0]

			for i in range(1,self.capas[1]):
				k=self.capas[1]-i
				a=np.dot(self.pesosI[:,:,k-1].transpose(), errI[:,k].transpose())
				errI[:, k-1]=a

		#calculo los deltas
		a=lr*errS.transpose()*outputs*(1-outputs)
		b=(self.valoresI[:,self.capas[1]-1])#.reshape(1,self.capas[2]))
		deltaS = a*b
		deltaSb = a

		deltaI = np.empty((self.capas[2], self.capas[2], self.capas[1]-1))
		deltaIb = np.empty((self.capas[2], self.capas[1]))

		if self.capas[1]==1:
			pass

		else:
			for i in range(1,self.capas[1]):
				b=(self.valoresI[:,i].reshape(1,self.capas[2]))
				a= lr*errI[:,i]*self.valoresI[:,i]*(1-self.valoresI[:,i])
				deltaI[:,:, i-1]=a*b
				deltaIb[:, i-1]= a

		a= lr*errI[:,0]*self.valoresI[:,0]*(1-self.valoresI[:,0])
		b= inputs

		deltaE= a.reshape(self.capas[2],1)*b
		deltaEb= a

		self.pesosE += deltaE
		self.pesosI += deltaI
		self.pesosS += deltaS
		self.biasE += deltaEb.reshape(self.capas[2],1)
		self.biasI += deltaIb
		self.biasS += deltaSb

		return 0


def lecturaJSON(a1, a2):
	x=a1
	contador=0
	datos=np.empty((1,12))

	for x in range(a1,a2):

		try:
			with open('new.json('+str(x)+')') as file:
		   		data = json.load(file)
		except FileNotFoundError:
			return 0

		array=np.empty((int(len(data['valores'])/11), 12))
		#array=np.empty((1,11))
		j=0
		i=0
		for valor in data['valores']:	
			temp=float(valor['id'])
			if j%11<8:
				if temp>350:
					temp=0.9
				else:
					temp=round(temp/400, 3)
			elif j%11<10:
				temp=round(temp/360, 3)
			elif j%11==10:
				if temp<0:
					array[i,11]=0.001
				else:
					array[i,11]=0.900
				if temp==0:
					temp=0.001
				elif abs(temp)>=29:
					temp=round((29/30)*abs(temp), 3)
				else:
					temp=round(abs(temp)/30,3)
				
			array[i,j%11]= temp	

			j+=1
			if j%11==0:
				i+=1
		datos=np.insert(datos, contador, array, axis=0)
		contador+=int(len(data['valores'])/11)
		
	return datos

def entrenarRed(datos, RN, contador):

	for i in range(contador):
		r=randint(0, len(datos)-1)
		entradas=np.empty((1,8))
		for j in range(8):
			entradas[0,j]=datos[r,j]
		target=np.array([(datos[r,10],datos[r,11])])
		RN.entrenarES(entradas, target)

def test(datos, RN, contador):
	error=0
	for i in range(contador):
		r=randint(0, len(datos)-1)

		entradas=np.empty((1,8))
		for j in range(8):
			entradas[0,j]=datos[r,j]

		print("resultado esperado: ", datos[r, 10], datos[r,11])
		print("resultado obtenido: ", RN.resultado(entradas))
		print(" ")
		#error+=RN.resultado(entradas)-datos[r,10]
	#error=error/contador
	#print("Error promedio: ", error)


