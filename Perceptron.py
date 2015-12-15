
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

	return k_0,k_1,k_2


def genera_datos(n):
	#matriz x de n renglones y 2 columnas valores entre 0 y 1
	x = np.random.rand(n,2)
	return x
	
def discriminante_lineal(k_0,k_1,k_2,x):
	
	Y = []
    for i in xrange(X.shape[0]):
        x_1 = X[i][1]
        x_2 = X[i][2]
        y.append(np.sign(k_0 + k_1 * x_1 + k_2 * x_2))
	return y

def PLA(X,Y):
	max_iter = 0
    w = np.random.uniform(0, 1, size=X.shape[1])
    Ye = np.sign(np.dot(X, w)) 
    error = Ye * Y
    
    while any(e != 1 for e in error) and max_iter < 1000:
        i = np.random.choice(X.shape[0])
        sign = np.sign(np.dot(X[i], w))

        if sign == Y[i]:
            pass
        else:
            w = w + np.dot(X[i], Y[i])
            Ye = np.sign(np.dot(X, w)) 
            error = Ye * Y
        max_iter += 1
    return w
	
def error_clasificacion(Y, Y_e):

    c = 0
    for i in xrange(len(Y)):
        if Y[i] != Y_e[i]:
            c += 1
    return c / float(len(Y))
	
def E_o_prom(n):

    E_lista = np.zeros(500)
    X_o = genera_datos(10000)

    for epoch in xrange(1, 100):
        k_0, k_1, k_2 = modelo_aleatorio()
        Y_o = discriminante_lineal(k_0, k_1, k_2, X_o)

        for iter in xrange(1, 100):
            X = genera_datos(N)
            Y = discriminante_lineal(k_0, k_1, k_2, X)
            w_0, w_1, w_2 = PLA(X, Y)
            Y_eo = discriminante_lineal(w_0, w_1, w_2, X_o)
            E_o = error_clasificacion(Y_o, Y_eo)
            indice = 100 * epoch + iter

    return sum(E_lista) / len(E_lista)