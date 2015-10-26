# -*- coding: utf-8 -*-

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

def E_o_prom(N):

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

            if len(E_lista) <= indice:
                temp = np.zeros(indice + 1)
                for i in xrange(0, len(E_lista)):
                    temp[i] = E_lista[i]
                temp[indice] = E_o
                E_lista = temp[:]
            else:
                E_lista[indice] = E_o

    return sum(E_lista) / len(E_lista)
    
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

print "Funcion 7: prueba E_o"
X_o = genera_datos(10000)
Y_o = discriminante_lineal(k_0, k_1, k_2, X_o)
Y_eo = discriminante_lineal(w_0, w_1, w_2, X_o)
E_o = error_clasificacion(Y_o, Y_eo)
print E_o

print "Funcion 8: pseudocodigo E_o_prom"
E_o_prom = E_o_prom(5)
print E_o_prom