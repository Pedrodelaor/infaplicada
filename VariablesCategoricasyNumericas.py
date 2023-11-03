#Capitulo 3 Analisis Estadisticos
#Este codigo son ejemplos de los tipos de Variables y tipos de Datos
#En estadistica una variable es una caracteristica o atributo que puede ser medida u observado.

#Las variables pueden ser clasificadas en:

###### VARIABLES CUALITATIVAS O CATEGORICAS:
#Son variables que toman valoresque representan una categoria o cualidad
# Variables nominales: cuando no hay un orden natural entre las categorias.
#(Ejemplo:color favorito,genero)
#Variables ordinales:cuando existe un orden natural entre las categorias.
#(Ejemplo:nivel educativo,calificacion escolar)


###### VARIABLES CUANTITATIVAS O NUMERICAS:
#Son variables que toman valores numericos
# Variables continuas: cuando pueden tomar cualquier valor dentro de un rango
#(Ejemplo:peso, altura)
#Variables discontinuas: cuando pueden tomar valores enteros
#(Ejemplo: numero de hijos, numero de animales en un zoologico)

# Variables cualitativas o categóricas
# Variables nominales
color_favorito = "Azul"
genero = "Masculino"

# Variables ordinales
nivel_educativo = "Licenciatura"
calificacion_escolar = "Aprobado"

# Variables cuantitativas o numéricas
# Variables continuas
peso = 70.5
altura = 175.3

# Variables discontinuas
numero_de_hijos = 2
numero_de_animales_en_zoologico = 50

# Imprimir los ejemplos de variables
print("Ejemplos de variables cualitativas o categóricas:")
print("Color favorito:", color_favorito, "Tipo:", type(color_favorito))
print("Género:", genero, "Tipo:", type(genero))

print("\nEjemplos de variables cuantitativas o numéricas:")
print("Nivel educativo:", nivel_educativo, "Tipo:", type(nivel_educativo))
print("Calificación escolar:", calificacion_escolar, "Tipo:", type(calificacion_escolar))
print("Peso:", peso, "Tipo:", type(peso))
print("Altura:", altura, "Tipo:", type(altura))
print("Número de hijos:", numero_de_hijos, "Tipo:", type(numero_de_hijos))
print("Número de animales en el zoológico:", numero_de_animales_en_zoologico, "Tipo:", type(numero_de_animales_en_zoologico))
