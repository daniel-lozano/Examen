# Ejercicio 3 (20 puntos)

# A través de fotos aéreas se tienen medidas del alcance de un lanzador de proyectiles. 
# Se tienen cuatro valores (en metros): 61, 115, 31, 117. Todas las mediciones tienen una incertidumbre de 5 metros. 
# El lanzador siempre da la misma velocidad inicial (entre 15 m/s y 60 m/s). 
# Los valores diferentes del alcance se deben a diferentes ángulos de lanzamiento. 
# Utilice métodos montecarlo y el teorema de Bayes para encontrar la velocidad más probable del lanzador de proyectiles 
# a medida que se va incluyendo información nueva sobre los valores del alcance.
# Haga una grafica (bayes.png) que tenga la probabilidad de la velocidad inicial dados los datos observacionales.
alcance=[61,115,31,117]
v_min=15
v_max=60
