
# Algoritmo PLA perceptro
# Rafael Noriega
import random
import numpy as np

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

modelo_aleatorio()