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

    for i in xrange(X.shape[0]):
        x_1 = X[i][1]
        x_2 = X[i][2]
        Y.append(np.sign(k_0 + k_1 * x_1 + k_2 * x_2))

    return Y

def PLA(X, Y):

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

print "Funcion 1: modelo_aleatorio"
k_0, k_1, k_2 = modelo_aleatorio()
print k_0
print k_1
print k_2

print "Funcion 2: genera_datos"
X = genera_datos(25)
print X

print "Funcion 3: discriminante_lineal"
Y = discriminante_lineal(k_0, k_1, k_2, X)
print Y

print "Funcion 4: PLA"
w_0, w_1, w_2 = PLA(X, Y)
print w_0
print w_1
print w_2

print "Funcion 5: error_clasificacion"
E_i = error_clasificacion(Y, Y)
print E_i

print "Funcion 6: prueba E_i"
k_0, k_1, k_2 = modelo_aleatorio()
X = genera_datos(10000)
Y = discriminante_lineal(k_0, k_1, k_2, X)
w_0, w_1, w_2 = PLA(X, Y)
Y_e = discriminante_lineal(w_0, w_1, w_2, X)
E_i = error_clasificacion(Y, Y_e)
print E_i