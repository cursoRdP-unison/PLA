# El algoritmo del perceptrón, y el error en muestra y fuera de muestra

# Introducción 

Esta práctica tiene como fin poner en relieve las ideas básicas de el aprendizaje, utilizando uno de los métodos de aprendizaje más antiguos y fáciles de implementar.

Esta práctica no intenta ser un remplazo del curso, por lo que se asume que los estudiantes conocen el algoritmo de aprendizaje del perceptrón (PLA por sus sigles en inglés), así como las ideas básicas sobre error en muestra y error fuera de muestra. Para esta práctica se puede realizar el problema en cualquier lenguaje de computación que conozca el estudiante. Sin embargo, se recomienda un lenguaje con capacidades de graficación, tal como *Matlab*, *R* y *Python* (con *numpy* y *matplotlib*).

Recordemos que el error fuera de muestra E_o es el error sobre todo el conjunto de puntos del espacio X. Una vez definido el criterio del error, el objetivo del aprendizaje es encontrar una hipótesis g en el conjunto de todas las hipótesis posibles que se pueden hacer con el método de aprendizaje. 

Lamentablemente, en todos los casos reales se desconoce E_o y lo más que se puede esperar es aproximarlo a partir del error en muestra E_i, el cual se define como el error medio de un conjunto de datos de aprendizaje disponibles. 

Para el caso del perceptrón, E_o es la esperanza que un dato se encuentre mal clasificado, y E_i es el porcentaje de datos mal clasificados por el perceptrón. Tambien sabemos, por lo visto en el curso, que si el conjunto de datos 
que se utiliza en el algoritmo de PLA es linealmente separable, entonces siempre se tiene una hipótesis final g tal que E_i = 0. 

Entonces, ¿Si E_i = 0, podríamos decir que el PLA aprende perfectamente? Desgraciadamente esto es falso. ¿Y eso porqué? Pues porque lo que nos interesa es E_o = 0 y no E_i = 0. Esta práctica tiene como fin dejar clara la diferencia entre E_i y E_o.

Para esto, vamos a hacer un poco de trampa, vamos a suponer que nosotros efectivamente conocemos la función  con la que se generaron los datos de aprendizaje, la cual va a ser una función del tipo `y = sign(k_0 + k_1 * x_1 + k_2 * x_2)`. Después vamos a generar datos con esta función, y vamos a estimar `g(x) = sign(w_0 + w_1 * x_1 + w_2 * x_2)` con el PLA. Así nosotros podemos hacer una estimación suficientemente aproximada de que tan grande es en general la diferencia entre E_i y E_o para diferente número de datos en el conjunto de aprendizaje.

## Práctica a realizar

1. Desarrolla una función `modelo_aleatorio` que devuelva 3 números aleatorios, el primero en el intervalo [0, 1] 
   y los otros dos en el intervalo [-1, 1] de forma que:
   ```
   k_0, k_1, k_2 = modelo_aleatorio()
   ```
   Por supuesto que la forma varia dependiendo del lenguaje en que se programe.
   
2. Desarrolla una función `genera_datos`tal que reciba un número entero positivo `N` y devuelva una matriz `X` 
   de `N`renglones y 2 columnas de manera que los valores de la matriz sean datos aleatorios en el intervalo [0, 1].
   ```
   X = genera_datos(N)
   ```

3. Desarrolla una función `discriminante_lineal` tal que reciba tres valores `k_0` `k_1` y `k_2` y  una matriz `X` de    2 por `N` y devuelva un vector `Y` de `N` elementos tales que por cada renglon `j` de la matriz X, se devuelva el 
   `j`-ésimo valor del vector `Y` tal que su valor sea `sign(k_0 + k_1 * x_1 + k_2 * x_2)`.
   ```
   Y = discriminante_lineal(k_0, k_1, k_2, X) 
   ```
   
4. Desarrolla una función `PLA` que implemente el algoritmo de aprendizaje del perceptrón para encontrar 
   `w_0`, `w_1` y `w_2`.
   ```
   w_0, w_1, w_2 = PLA(X, Y)
   ```
   
5. Desarrolla una función `error_clasificacion` que reciba un vector de valores `Y`y un vector de valores `Y_e` y 
   calcule el porcentaje de valores diferentes entre ambos vectores
   ```
   e = error_clasificacion(Y, Y_e)
   ```

6. Prueba que el conjunto funciona, esto es, para diferentes valores de `N`y repetidos tantas veces 
   como sea necesario al realizar lo siguiente:
   ```
   k_0, k_1, k_2 = modelo_aleatorio()
   X = genera_datos(N)
   Y = discriminante_lineal(k_0, k_1, k_2, X)
   w_0, w_1, w_2 = PLA(X, Y)
   Y_e = discriminante_lineal(w_0, w_1, w_2, X)
   E_i = error_clasificacion(Y, Y_e)
   ```
   en todos los casos `e` debe de ser 0 o un valor muy cercano (como `1e-12`).
   
7. `E_i` Es en este caso el error en muestra, que es el que se obtiene de verificar el error que el clasificador
   (descrito por `w_0`, `w_1` y `w_2`) presenta respecto a los datos reales, pero únicamente de datos de aprendizaje.
   
   Este error no es exactamente el error fuera de muestra, y para calcular dicho error en el plano [0, 1] x [0, 1]
   hay que realizar algunas operaciones de geometría analítica que no siempre son sencillas. Por esta razón vamos a
   considerar estimar el E_out, con un conjunto de datos sensiblemente mayor al que utilizamos para el aprendizaje.
   por ejemplo:
   ```
   X_o = genera_datos(10000)
   Y_o = discriminante_lineal(k_0, k_1, k_2, X_o)
   Y_eo = discriminante_lineal(w_0, w_1, w_2, X_o)
   E_o = error_clasificacion(Y_o, Y_eo)
   ```
   
8. Ahora vamos a comparar con un número diferente de datos de aprendizaje, como E_o cambia en terminos generales. 
   Con el fin de generalizar, haga una función que reciba un valor `N` y devuelva un `E_o_prom` estimado de la 
   siguiente forma:
   ```
   Entrada: N
   Salida: E_o_prom
   
   E_lista = arreglo e numeros de 500 espacios
   X_o = genera_datos(10000)

   para epoch de 1 a 100:
      k_0, k_1, k_2 = modelo_aleatorio()
      Y_o = discriminante_lineal(k_0, k_1, k_2, X_o)

      para iter de 1 a 100:
          X = genera_datos(N)
          Y = discriminante_lineal(k_0, k_1, k_2, X)
          w_0, w_1, w_2 = PLA(X, Y)
          Y_eo = discriminante_lineal(w_0, w_1, w_2, X_o)
          E_o = error_clasificacion(Y_o, Y_eo)
          E_lista[100 * epoch + iter] = E_o
      fin para

   fin para

   devuelve el valor promedio de los valores de E_lista
   ```
   Como puede verse en el pseudocódigo, la idea es poder estimar en forma general el error promedio entre el 
   E_i y el E_o que tendríamos si tuvieramos solo `N` datos de aprendizaje. 

9. Explica en forma gráfica que es lo que se está haciendo y que es el valor que estamos midiendo.

10. Realiza una tabla con los valores de `E_o_prom`para `N` que tome los valores de 10, 20, 50, 100, 500 
    respectivamente. Escribe claramente tus conclusiones de este trabajo. 

