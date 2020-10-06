import numpy as np 
import math 
from random import randint, random
from time import sleep
import json

#funciones de activacion

def sigmoid(matrix): #aplica la funcion sigmoid a todos los componentes de una matriz

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

def TanH(matrix): #aplica pla funcion Hiper Tangente a todos los componentes de una matriz
	for i in range(len(matrix)):
		a=math.exp(matrix[i])
		b=np.exp(-matrix[i])
		matrix[i]= (a-b)/(a+b)
	return matrix

#funciones de matriz

def mutarMatiz(matrix, rate): #"muta" una matriz
	#llamamos mutar a cambiar un porcentaje de la matriz por componentes aleatorios
	#este porcentaje esta dado por el ratio

	s=np.shape(matrix)

	#primero recorremos uno a uno los componentes de la matriz
	for i in range(s[0]):
		for j in range(s[1]):

			if len(s)==2:
				prob= random() #se toma un numero random del 0 al 1
				if prob < rate:
				#si es más chico que el ratio se muta el componente de la matriz
				#mientras más chico el ratio menos probable que se cumpla esta condicion	
					matrix[i,j]=random()
				else:
					pass

			else:
				#el esta parte tenemos el mismo codigo
				#pero agregamos un for mas si la matriz es de 3 dim
				for h in range(s[2]):
					prob= random()
					if prob < rate:
						matrix[i,j,h]=random()
					else:
						pass
	
	return matrix

#Red neuronal

class RedNeuronal():

	def __init__(self, capas, lr):

		self.capas=capas
		self.lerningR=lr

		#iniciar los pesos de forma aleatoria
		#primera capa de la red
		self.biasE=np.random.random((capas[2],1))
		self.pesosE=np.random.uniform(0.0001, (1/math.sqrt(capas[0])),(capas[2], capas[0]))		

		#capas intermedias
		self.biasI=np.random.random((capas[2],capas[1]))
		self.pesosI=np.random.uniform(0.0001, (1/math.sqrt(capas[2])),(capas[2], capas[2], capas[1]-1))
		self.valoresI=np.empty((capas[2], capas[1]), dtype=float)

		#ultima capa de la red
		self.biasS=np.random.random((capas[3],1))
		self.pesosS=np.random.uniform(0.0001, (1/math.sqrt(capas[2])),(capas[3], capas[2])) 

	def mutar(self, rate): #mutamos la red total 
		#mutamos cada matriz de la red por separado
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

		lr=self.lerningR

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
		b=(self.valoresI[:,self.capas[1]-1])
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

		#print(deltaS)
		#print(deltaSb)
		self.pesosE += deltaE
		self.pesosI += deltaI
		self.pesosS += deltaS
		self.biasE += deltaEb.reshape(self.capas[2],1)
		self.biasI += deltaIb
		self.biasS += deltaSb
		return 0


# funciones para entrenar la red

def lecturaJSON(a1, a2): #con esta funcion tomamos los datos de los archivos json
	#tiene dos parametros donde determinamos que rango de archivos queremos tomar
	#ejemplo: (0, 10) toma del archivo 0 al 10
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
			#estos if son para normalizar los valores entre 0 y 1
			if j%11<8:
				if temp>320:
					temp=320/400
				else:
					temp=round(temp/400, 5)
			elif j%11<10:
				temp=round(temp/360, 5)

			elif j%11==10:

				if temp<0:
					array[i,11]=0.2
				else:
					array[i,11]=0.8

				temp+=30
				temp=round(temp/60, 5)
				if temp>=0.95:
					temp=0.95
				elif temp<=0.05:
					temp=0.05
				
			array[i,j%11]= temp	

			j+=1
			if j%11==0 and j!=0:
				i+=1
		#guardamos los datos en una unica matriz
		datos=np.insert(datos, contador, array, axis=0) 
		contador+=int(len(data['valores'])/11)+1
		
	return datos

def entrenarRed(datos, RN, contador): #con esta funcion entreno la red
	#el primer parametro es la matriz que contiene la informacion para entrenar la red
	#el segundo es la red a entrenar
	#el contador es la cantidad de veces que se entrena 

	for i in range(contador):
		#los ejemplos los tomamos de forma aleatoria
		r=randint(0, len(datos)-2)
		entradas=np.empty((1,RN.capas[0]))
		for j in range(RN.capas[0]):
			entradas[0,j]=datos[r,j]
		target=np.array([(datos[r,10])])#,datos[r,11])])
		RN.entrenarES(entradas, target)

def test(datos, RN, contador): #con esta funcion testeo la red
	#el primer parametro es la matriz que contiene la informacion para testear la red
	#el segundo es la red a testear
	#el contador es la cantidad de veces que se testea

	for i in range(contador):
		r=randint(0, len(datos)-2)

		entradas=np.empty((1,RN.capas[0]))
		for j in range(RN.capas[0]):
			entradas[0,j]=datos[r,j]

		print("resultado esperado: ", datos[r, 10])#, datos[r,11])
		print("resultado obtenido: ", RN.resultado(entradas))
		print(" ")
