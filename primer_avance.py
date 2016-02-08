import numpy as np
import matplotlib.pyplot as plt
import sys

import random as r
import math
from matplotlib.pylab import hist, show, figure

#Tarea2


##############################################################
##Ejercicio 1
#Desarrolla una funcion modelo_aleatorio en el cual:
#a. Se soliciten 4 numeros aleatorios entre el 0 y el 1, a los que llamaremos x1, y1, x2, y2.
#b. Se obtenga el valor de os pesos de la recta que pasa entre los dos puntos calculados como: k_2 = 1 k_1 = (y2 - y1) / (x2 - x1) k_0 = y_1 - k_1 * x_1 
#de forma que:
#k_0, k_1, k_2 = modelo_aleatorio()
##############################################################
def modelo_aleatorio():
    #se crea una matriz de 2,2 para obternet 4 elementos aleatorios
    n=np.random.rand(2,2)
    print n

    x1=n[0][0]
    x2=n[0][1]
    y1=n[1][0]
    y2=n[1][1]
    print x1
    print x2
    print y1
    print y2

    k_2 = 1
    k_1 = (y2 - y1) / (x2 - x1)
    k_0 = y1 - k_1 * x1

    #print "primero: ",k_0,":",k_1,":",k_2
       
    return k_0,k_1,k_2
k_0,k_1,k_2=modelo_aleatorio()

print "Ejercicio1"
print "k_0:",k_0,"k_1:",k_1,"k_2:",k_2


################################################################################################
#Ejercicio 2
#Desarrolla una funcion genera_datos tal que reciba un numero entero positivo N 
#y devuelva una matriz X de Nrenglones y 2 columnas de manera que los valores de la matriz sean datos aleatorios en el intervalo [0, 1].
#X = genera_datos(N)
#################################################################################################
def genera_datos(numero): 
   
    #Nrenglones y 2 columnas de manera que los
    #valores de la matriz sean datos aleatorios en el intervalo [0, 1].
    n=np.random.rand(numero,2)
    return n

N=5
X=genera_datos(N)
print "Ejercicio 2"
print X


###############################################################################
#Problema 3

##Desarrolla una funcion discriminante_lineal tal que reciba tres valores k_0 k_1 y k_2
#y una matriz X de 2 por N y devuelva un vector Y de N elementos tales que por cada renglon j 
#de la matriz X, se devuelva el j-esimo valor del vector Y tal que su valor sea sign(k_0 + k_1 * x_1 + k_2 * x_2).
#Y = discriminante_lineal(k_0, k_1, k_2, X)
#############################################################################
#N=6
#X = np.matrix(np.arange(12).reshape((N, 2)))




def discriminante_lineal(k_0,k_1,k_2,X): 

 
    #print X
    #define el num de renglones en la matriz
    nrows=len(X[:,1])
    Y=[i for i in range(nrows)]

    Y=np.array(Y)
    for j in xrange(nrows):

      Y[j]=np.sign(k_0+k_1*X[j,0]+k_2*X[j,1])

    
    return Y
   
    #Nrenglones y 2 columnas de manera que los
    #valores de la matriz sean datos aleatorios en el intervalo [0, 1].
    #   n=np.random.rand(numero,2)

Y=discriminante_lineal(1,2,3,X)


print "Y:", Y
#numpy.sign
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.sign.html
