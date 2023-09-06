#TAREA 3. Hacer 5 ejercicios de cadenas.

###Ejercicio 1. Cadena utilizando: format() formatea la cadena en una salida más agradable
# # format() formatea la cadena en una salida más agradable
nombre = 'Pedro'
apellido = 'De La O'
ocupacion = 'Estudiante de ingeniería electrónica industrial'
pais = 'México'
oracion = 'Soy {} {}. Soy un {}. Vivo en {}.'.format(nombre, apellido, ocupacion, pais)
print("Ejercicio 1. Cadena utilizando: format() formatea la cadena en una salida más agradable")
print("Datos:",oracion) # Datos: Soy Pedro De La O. Soy un Estudiante de ingeniería electrónica industrial. Vivo en México.

###Ejercicio 2. Cadena utilizando:  endswith (): verifica si una cadena termina con un final específico y devuelve un bool (True/False)
# endswith (): verifica si una cadena termina con un final específico y devuelve un bool (True/False)

parrafo = 'La UAZ es la mejor universidad del estado de Zacatecas'
print("Ejercicio 2. Cadena utilizando:  endswith (): verifica si una cadena termina con un final específico y devuelve un bool (True/False)")
print('Parrafo:', parrafo)
print("¿El parrafo termina en Zacatecas?:",parrafo.endswith('Zacatecas')) # True
print("¿El parrafo termina en Aguacalientes?:",parrafo.endswith('Aguascalientes')) # False


###Ejercicio 3. Cadena utilizando: replace (): reemplaza la subcadena dentro

frase = 'Algunos sabemos programar en python, y otros sabemos programar en C++'
print("Ejercicio 3. Cadena utilizando: replace (): reemplaza la subcadena dentro")
print('Frase:', frase)
print("Reemplaza la palabra python de la frase original por la palabra JavaScrpt:",frase.replace('python', 'JavaScript')) # Algunos sabemos programar en JavaScript, y otros sabemos programar en C++


###Ejercico 4. Cadena utilizando: swapcase(): Cambia de mayuscula a minuscula y viceversa
  
oración = 'la computadora es un dispositivo electrónico que nos permite procesar y manipular la información'
print("Ejercico 4. Cadena utilizando: swapcase(): Cambia de mayuscula a minuscula y viceversa")
print('Oración:', oración)
print("Cambia de mayuscula a minuscula y viceversa de la Oración:",oración.swapcase()) #  LA COMPUTADORA ES UN DISPOSITIVO ELECTRÓNICO QUE NOS PERMITE PROCESAR Y MANIPULAR LA INFORMACIÓN


###Ejercicio 5. Cadena utilizando Cadena multilínea

cadena_multilinea = "Los sistemas compuacionales se componen de:\n Software\n Hardware\n Inteligencia Artificial\n Arquitectura de Computadoras\n Automatización\n Redes de Internet\n"
print("Ejercicio 5. Cadena utilizando Cadena multilínea")
print ("Cadena Multilinea:",cadena_multilinea) # El resultado es una cadena de multiples lineas: