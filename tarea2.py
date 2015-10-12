#matplotlib inline
#enconding: utf-8
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


print "hp"
#numpy.sign
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.sign.html

###############################################################################
#Problema 4

#Desarrolla una funcion PLA que implemente el algoritmo de aprendizaje del perceptron
#para encontrar w_0, w_1 y w_2.
#w_0, w_1, w_2 = PLA(X, Y)
################################################################################

def PLA(X,Y):
    threshold = 0.5
    learning_rate = 0.1
    weights = [0, 0, 0]
    training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 0)]


    print "antes de la funcion"
    print training_set
    print "despues"

    def dot_product(values, weights):
        return sum(value * weight for value, weight in zip(values, weights))

    while True:
        print('-' * 60)
        error_count = 0
        for input_vector, desired_output in training_set:
            print(weights)
            result = dot_product(input_vector, weights) > threshold
            error = desired_output - result
            if error != 0:
                error_count += 1
                for index, value in enumerate(input_vector):
                    weights[index] += learning_rate * error * value
        if error_count == 0:
            break

    
    w_0= weights[0]
    w_1= weights[1]
    w_2= weights[2]
    return w_0,w_1,w_2 
#w_0,w_1,w_2=PLA()

    ###############################################
#Problema 5

#Desarrolla una funcion error_clasificacion que reciba un vector de valores 
#Yy un vector de valores Y_e y calcule el porcentaje de valores diferentes entre ambos vectores
#e = error_clasificacion(Y, Y_e)
###############################################

print "problema 5"

Y1=[i for i in range(20)]
Y1=np.array(Y1)

Y2=[i for i in range(10,30)]
Y2=np.array(Y2)

#print "aaaaaaaaaaaaaa"
#print Y1
#print Y2

def error_clasificacion(Y,Y_e):

    error1=0
    n=len(Y)  
    for i in range(n):
        if(Y[i]!=Y_e[i]):error1=error1+1

     

    percent=(error1/n)*100
    return percent

e=error_clasificacion(Y1,Y2)
print "error de clasificacion"
print e




###############################################
#Problema 6


#Prueba que el conjunto funciona, esto es, para diferentes valores de Ny repetidos tantas veces como sea necesario al realizar lo siguiente:

#k_0, k_1, k_2 = modelo_aleatorio()
#X = genera_datos(N)
#Y = discriminante_lineal(k_0, k_1, k_2, X)
#w_0, w_1, w_2 = PLA(X, Y)
#Y_e = discriminante_lineal(w_0, w_1, w_2, X)
#E_i = error_clasificacion(Y, Y_e)
#en todos los casos e debe de ser 0 o un valor muy cercano (como 1e-12).

#########################################################

k_0, k_1, k_2 = modelo_aleatorio()
X = genera_datos(N)
Y = discriminante_lineal(k_0, k_1, k_2, X)
w_0, w_1, w_2 = PLA(X, Y)
Y_e = discriminante_lineal(w_0, w_1, w_2, X)
E_i = error_clasificacion(Y, Y_e)

print "PROBLEMA 6"
print "E_i:"
print E_i



#################################################
#Problema 7

#E_i Es en este caso el error en muestra, que es el que se obtiene de verificar el error que el clasificador (descrito por w_0, w_1 y w_2)
# presenta respecto a los datos reales, pero unicamente de datos de aprendizaje.

#Este error no es exactamente el error fuera de muestra, y para calcular dicho error en el plano [0, 1] x [0, 1] 
#hay que realizar algunas operaciones de geometria analitica que no siempre son sencillas.
# Por esta razon vamos a considerar estimar el E_out, con un conjunto de datos sensiblemente mayor al que utilizamos para el aprendizaje. por ejemplo:

X_o = genera_datos(10000)
Y_o = discriminante_lineal(k_0, k_1, k_2, X_o)
Y_eo = discriminante_lineal(w_0, w_1, w_2, X_o)
E_o = error_clasificacion(Y_o, Y_eo)

print "PROBLEMA 7"
print "E_o:"
print E_o