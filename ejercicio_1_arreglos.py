"""
1.Calcular la media, mediana y desv.estandar de un conjunto de datos:
"""

import numpy as np


#Crear una lista de datos
datos = np.array([5,7,8,9,10,11,12,14,15,16])

#Calcular media
mean_datos = np.mean(datos)

#Calcular mediana
mediana = np.median(datos)

#Calcular desviacion estandar
desv_estan = np.std(datos)

print("la media de los datos es igual a:", mean_datos)
print("la mediana de los datos es igual a:", mediana)
print("la desviacion estandar de los datos es igual a:", desv_estan)
