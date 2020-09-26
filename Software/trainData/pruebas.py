from RedNeuronal import RedNeuronal, test
import numpy as np
from random import randint

capas= np.array([2,1,3,2])
RN= RedNeuronal(capas)

trainData= np.array([
	(0.01, 0.01, 0.1, 0.5),
	(0.90, 0.01, 0.1, 0.1),
	(0.01, 0.90, 0.1, 0.9),
	(0.90, 0.90, 0.9, 0.9)])

for i in range(5000):
	r= randint(0,len(trainData)-1)
	entradas=np.array([trainData[r,0], trainData[r,1]])
	target= np.array(trainData[r,0],trainData[r,0])
	RN.entrenarES(entradas, target)

for i in range(4):
	entradas=np.array([trainData[i,0], trainData[i,1]])
	print(trainData[i,0], trainData[i,1])
	print(RN.resultado(entradas))


