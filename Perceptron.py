__author__ = 'JuanManuel'

import numpy as np
import matplotlib.pyplot as plt

def modelo_aleatorio():

	x1 = np.random.uniform(0,1)
	y1 = np.random.uniform(0,1)
	x2 = np.random.uniform(0,1)
	y2 = np.random.uniform(0,1)

	k_2 = 1 
	k_1 = (y2 - y1) / (x2 - x1) 
	k_0 = y1 - k_1 * x1 

	return k_0, k_1, k_2

def genera_datos(N):
	return None if N <= 0 else np.random.uniform(0, 1, size=(N,2))
	
k_0, k_1, k_2 = modelo_aleatorio()

X = genera_datos(5)