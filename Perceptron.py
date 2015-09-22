__author__ = 'JuanManuel'

import numpy as np
import matplotlib.pyplot as plt

def modelo_aleatorio():

	x1 = np.random.uniform(0,1)
	y1 = np.random.uniform(0,1)
	x2 = np.random.uniform(0,1)
	y2 = np.random.uniform(0,1)

	k_2 = 1.0 
	k_1 = (y2 - y1) / (x2 - x1) 
	k_0 = y1 - k_1 * x1 

	return k_0, k_1, k_2

def genera_datos(N):

	return None if N <= 0 else np.column_stack((np.ones(N), (np.random.uniform(0, 1, size=(N, 2)))))

def discriminante_lineal(k_0, k_1, k_2, X):

	Y = []
	temp = 0

	for i in xrange(X.shape[0]):
		x_1 = X[i][0]
		x_2 = X[i][1]
		Y.append(np.sign(k_0 + k_1 * x_1 + k_2 * x_2))

	return Y

def PLA(X, Y):

	w = np.random.uniform(0, 1, size=3)

	rand = 
	Xi = X[np.random.choice(X.shape[0])]

	z = np.dot(w.transpose(), Xi)

	print z
		
k_0, k_1, k_2 = modelo_aleatorio()

X = genera_datos(5)

Y = discriminante_lineal(k_0, k_1, k_2, X)

PLA(X, Y)
