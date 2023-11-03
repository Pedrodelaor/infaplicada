"""
Tenemos tupla(), lista[] y diccionario{}
Lo primero es importar las librerias para utilizar sus funciones ya hechas

"""
import statistics as stat
import numpy as np


#Crear una lista de datos
datos = np.array([10,12,15,18,20,22,24,28,30,30])

#Calcular media
mean_datos = np.mean(datos)

#Calcular mediana
mediana = np.median(datos)

#Calcular moda
   #moda = np.mode(datos)
moda_dos = stat.mode(datos)

#Calcular la varianza
varianza = np.var(datos)

#Calcular desviacion estandar
desv_estan = np.std(datos)

print("la media de los datos es igual a:", mean_datos)
print("la mediana de los datos es igual a:", mediana)
print("la moda de los datos es igual a:", moda_dos)
print("la varianza de los datos es igual a:", varianza)
print("la desviacion estandar de los datos es igual a:", desv_estan)
