import numpy as np
import random
def modelo_aleatorio():
    print "Introduce 4 valores aleatorios del 0 al 1"
    x1 = (float)(raw_input("X1: "))
    y1 = (float)(raw_input("y1: "))
    x2 = (float)(raw_input("X2: "))
    y2 = (float)(raw_input("y2: "))
    k1 = (y2 - y1) / (x2 - x1)
    k0 = y1 - k1 * x1
    return k0, k1, 1

def genera_datos(N):
    aux = np.random.randn(N, 3)
    for i in range(0, N):
        aux[i][0] = 1
    print aux
    return aux

def discriminante_lineal(k_0, k_1, k_2, X):
    Y = np.arange(len(X))
    for j in range(0, len(X)):
        Y[j] = np.sign(k_0 + k_1 * X[j, 0] + k_2 * X[j, 1])
    print Y
    return Y

def PLA(X, Y):
    W = np.ones((3, 1))
    while True:
        y_ = np.sign(X.dot(W))
        ind = np.where(Y - y_ > 0)
        if len(ind) == 0:
            return W[0], W[1], W[2]
        i = np.random.choice(len(ind))
        W += Y[i] * X[i,:]
        W.T

def error_clasificacion(Y, Y_e):
    aux = np.where((Y - Y_e) > 0)
    return len(aux)/len(Y)

k_0, k_1, k_2 = modelo_aleatorio()
X = genera_datos(5)
Y = discriminante_lineal(k_0, k_1, k_2, X)
w_0, w_1, w_2 = PLA(X, Y)
Y_e = discriminante_lineal(w_0, w_1, w_2, X)
E_i = error_clasificacion(Y, Y_e)
