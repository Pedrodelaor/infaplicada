"""
2.Calcular el coeficiente de variacion de un conjunto de datos:
"""

import numpy as np

#Crear una lista de datos
datos = np.array([5,7,8,9,10,11,12,14,15,16,17,18,19,20])

#Calcular desviacion estandar
desv_estan = np.std(datos)

#Calcular media
mean_datos = np.mean(datos)

#Calcular el coeficiente de variacion (C.V.) de un conjunto de datos
#Utilizando la formula, primero se saca la desviacion estandar y despues la media
#Y se aplica esta formula: c.v. = (desv_estan / mean_datos) * 100

coeficiente_variacion = (desv_estan / mean_datos) * 100


print("la media de los datos es igual a:", mean_datos)
print("la desviacion estandar de los datos es igual a:", desv_estan)
print("el coeficiente de variacion de los datos es:", coeficiente_variacion )
