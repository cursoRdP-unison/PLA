
# Algoritmo PLA perceptro
# Rafael Noriega
import numpy as np
import random


def modelo_aleatorio():
	#numeros aleatorios entre cero y uno
	"""
	x1 = random.uniform(0, 1)
	y1 = random.uniform(0, 1)
	x2 = random.uniform(0, 1)
	y2 = random.uniform(0, 1)
	"""

	# mejor forma de hacerlo!
	x1,y1,x2,y2 = [random.uniform(0,1) for i in range(4)]
	print x1
	print x2
	print y1
	print y2

	#creo qu es de otra forma? y no asi algo no me cuadra del todo
	k_2 = 1
	k_1 = (y2-y1)/(x2-x1)
	k_0 = y1-k1*x1

#modelo_aleatorio()

def genera_datos(n):
	#matriz x de n renglones y 2 columnas valores entre 0 y 1
	x = np.random.rand(n,2)

matriz=genera_datos(2)
print matriz

def discriminante_lineal(k_0,k_1,k_2):# falta recibir la matriz
	
	np.sign(k_0 + k_1 * x1 + k_2 * x2)

def PLA():
	#me falta mucho :(

def error_clasificacion():