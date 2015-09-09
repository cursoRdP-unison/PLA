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




