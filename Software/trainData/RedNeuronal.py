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
				try:
					matrix[i,j]= 1/(1+math.exp(-matrix[i,j]))
				except OverflowError:
					print(matrix[i,j])
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
		outputs=TanH(np.dot(self.pesosS, valoresIO.reshape(len(valoresIO),1))+self.biasS)
		return outputs

	def entrenarES(self, inputs, respuestas):
	
		outputs= self.resultado(inputs)
		respuestas=respuestas.astype(np.float)

		lr=0.2

		#caculo los errores de todos las capas
		errS= respuestas.transpose()-outputs.transpose()

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

		deltaS = lr*errS.transpose()*(1-(outputs*outputs))*(self.valoresI[:,self.capas[1]-1].reshape(1,self.capas[2]))
		deltaSb = lr*errS.transpose()*(1-(outputs*outputs))

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

def lecturaJSON():
	div=11
	x=0
	while True:
		try:
			with open('new.json('+str(x)+')') as file:
		   		data = json.load(file)
		except FileNotFoundError:
			break

		#print(data)
		array= np.empty((int(len(data['valores'])/div),div))
		
		i=j=0
		for valor in data['valores']:
			array[i,j%div]=(int(valor['id']))
			
			if j%div<8:
				array[i,j%div]=array[i,j%div]/400
			if j%div==8 or j%div==9:
				array[i,j%div]=array[i,j%div]/360
			if j%div==10:
				if array[i,j%div]==0:
					array[i,j%div]=0.01
				else:
					array[i,j%div]=array[i,j%div]/30

			j+=1

			if j%div==0 and j!=0:
				i+=1
		x+=1
	return array

capas= np.array([10,8,8,1])
RN= RedNeuronal(capas)

trainData=lecturaJSON()
#print(trainData)

for i in range(1000):
	r=randint(5,len(trainData)-5)
	inputs=np.empty((1,10))
	for j in range(10):
		inputs[0,j]=trainData[r,j]
	salida=trainData[r,10]/30
	RN.entrenarES(inputs, salida)

r=randint(5,len(trainData)-5)
inputs=np.empty((1,10))
for j in range(8):
	inputs[0,j]=trainData[r,j]/400
inputs[0,8]=trainData[r,8]/360
inputs[0,9]=trainData[r,9]/360
salida=trainData[r,10]/30
print(RN.resultado(inputs))
print(salida)