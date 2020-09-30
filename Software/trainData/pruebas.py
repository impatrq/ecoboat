from RedNeuronal import RedNeuronal, test
import numpy as np
from random import randint

capas= np.array([2,3,3,2])
RN= RedNeuronal(capas)

trainData= np.array([
	(0.01, 0.01, 0.1, 0.1),
	(0.90, 0.01, 0.1, 0.1),
	(0.01, 0.90, 0.1, 0.9),
	(0.90, 0.90, 0.9, 0.9)])

for i in range(10000):
	r= randint(0,len(trainData)-1)
	entradas=np.array([trainData[r,0], trainData[r,1]])
	target= np.array([trainData[r,2], trainData[r,3]])
	RN.entrenarES(entradas, target)

for i in range(4):
	entradas=np.array([trainData[i,0], trainData[i,1]])
	print(trainData[i,2], trainData[i,3])
	print(RN.resultado(entradas))


