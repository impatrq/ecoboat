import numpy as np 
import math 
from time import sleep

def sigmoid(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix[i,j]= 1/(1+math.exp(-matrix[i,j]))
	return matrix

def sigmoid1(matrix):
	for i in range(len(matrix)):
		matrix[i]= 1/(1+math.exp(-matrix[i]))
	return matrix

class RedNeuronal():

	def __init__(self, capas):

		self.capas=capas

		#iniciar los pesos de forma aleatoria
		#primera capa de la red
		self.biasE=np.random.random((capas[2],1))
		self.pesosE=np.random.random((capas[2], capas[0]))		

		#capas intermedias
		self.biasI=np.random.random((capas[2],capas[1]))
		self.pesosI=np.random.random((capas[2], capas[2], capas[1]))
		self.valoresI=np.empty((capas[2], capas[1]), dtype=float)

		#ultima capa de la red
		self.biasS=np.random.random((capas[3],1))
		self.pesosS=np.random.random((capas[3], capas[2])) 

	def adivinar(self, inputs):

		inputs=inputs.astype(np.float)
		inputs=inputs.reshape(self.capas[0],1)
		#pesos de capas intermedias
		a=sigmoid(np.dot(self.pesosE, inputs)+self.biasE)
		for i in range(len(self.valoresI[:,0])):	
			self.valoresI[i,0]=a[i,0]

		if self.capas[1]>1:
			for i in range(0,self.capas[1]-1):
				a=sigmoid1(np.dot(self.pesosI[:,:,i], self.valoresI[:,i])+self.biasI[:,i])
				for j in range(0,self.capas[2]):
					self.valoresI[j, i+1]=a[j]
			
		#ultima capa
		outputs=sigmoid1(np.dot(self.pesosS, self.valoresI[:,self.capas[1]-1])+self.biasS)
		return outputs

	def entrenar(self, inputs, respuestas):
		outputs= self.adivinar(inputs)
		return outputs


a=np.array([1,3,5,4])
cap=np.array([4,3,2,1])

nn=RedNeuronal(cap)
print(nn.entrenar(a, 1))
