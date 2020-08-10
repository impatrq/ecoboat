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

def TanH(matrix):
	for i in range(len(matrix)):
		a=math.exp(matrix[i])
		b=np.exp(-matrix[i])
		matrix[i]= (a-b)/(a+b)
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
		self.pesosI=np.random.random((capas[2], capas[2], capas[1]-1))
		self.valoresI=np.empty((capas[2], capas[1]), dtype=float)

		#ultima capa de la red
		self.biasS=np.random.random((capas[3],1))
		self.pesosS=np.random.random((capas[3], capas[2])) 

	def adivinar(self, inputs):


		#filtros de las entradas

		#filtro para US
		for i in range (8):
			inputs[i]=inputs[i]/400
		#filtro para curso deseado
		inputs[8]=(inputs[8]+180)/360

		inputs=inputs.astype(np.float)
		inputs=inputs.reshape(self.capas[0],1)

		#pesos de capas intermedias
		a=sigmoid(np.dot(self.pesosE, inputs)+self.biasE)
		self.valoresI[:,0]=a[:,0]

		if self.capas[1]>1:
			for i in range(self.capas[1]-1):
				a=sigmoid1(np.dot(self.pesosI[:,:,i], self.valoresI[:,i])+self.biasI[:,i])
				self.valoresI[:, i+1]=a
				
			
		#ultima capa
		valoresIO= self.valoresI[:,self.capas[1]-1]
		outputs=TanH(np.dot(self.pesosS, valoresIO.reshape(len(valoresIO),1))+self.biasS)
		return outputs


	def entrenar(self, inputs, respuestas):
	
		outputs= self.adivinar(inputs)
		respuestas=respuestas/float(60)

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
		deltaEb= a.reshape(self.capas[2],1)

		self.pesosE += deltaE
		self.pesosI += deltaI
		self.pesosS += deltaS
		self.biasE += deltaEb
		self.biasI += deltaIb
		self.biasS += deltaSb

		return 0

cap=np.array([4,3,2,3])
inp=np.array([(1,3,5,4)])
resp=np.array([1,0.8,0.5])
nn=RedNeuronal(cap)

print(nn.adivinar(inp))
for i in range(1000):
	nn.entrenar(inp, resp)
print(nn.adivinar(inp))