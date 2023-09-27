#Examen Informática Aplicada.
#Dar solución a los siguientes problemas:


print('1. Crear una lista, agregar un elemento, y posteriormente acceder a un elemento en la lista.')
bandas_de_rock =['Mana','Caifanes','Soda Estereo','Panteon Rococo','El TRI','Molotov','Moderatto','Guns and Roses']
print('Lista de bandas de rock:', bandas_de_rock)
bandas_de_rock.append('Cafe Tacuva')
print('Lista con un elemento agregado, una nueva banda', bandas_de_rock)
segunda_banda= bandas_de_rock[1]
print('Accedemos a ver cual es la segunda banda de la lista:', segunda_banda)

print('2. Crear dos conjuntos y realizar operaciones de conjuntos: unión e intersección.')
clima_semana1 = {'soleado', 'nublado', 'calido', 'frio', 'soleado','nublado','soleado'}
clima_semana2 = {'frio', 'nublado','frio', 'soleado','nublado','calido','lluvioso'}
clima_quincena1 = clima_semana1.union(clima_semana2)
print('La union de los dos conjuntos del clima de las dos semanas es:', clima_quincena1)
interseccion_climaquincena1 = clima_semana1.intersection(clima_semana2)
print('La interseccion de los climas en ambas semanas es:', interseccion_climaquincena1)

print('3. Crear un diccionario, acceder a uno de sus valores y modificar elementos en el diccionario.')
series = {'canal1':'The Flash', 'canal2':'Arrow', 'canal3':'Malcolm', 'canal4':'Gotham'}
print('Canal y su serie de television:', series)
print('La serie del canal 4 es:',series['canal4'])
series['canal3'] = 'The walking Dead'
print('La nueva lista de series modificada es:', series)


print('4. Crea una lista con 10 elementos numéricos desordenados, y realiza un código para:')
numeros_desordenados = ['7','3','8','1','0','2','5','9','4','6']
print('los numeros desordenados son:', numeros_desordenados)
####a. Ordenarlos de manera ascendente
numeros_desordenados.sort()
print('los numeros ordenados de manera ascendente son:', numeros_desordenados)
 
####b. Ordenarlos de manera descendente
numeros_desordenados.sort(reverse=True)
print('Los numeros ordenados de manera descendente son:', numeros_desordenados) 
####c. Sumar todos los elementos de la lista con un “for”.


print('5. Crear una lista de elementos, y comprobar si un elemento está en la lista utilizando un “if”.')
canciones = ['rojo','amarillo','verde','morado','blanco','naranja','azul','negro']
print('Album colores JBalvin', canciones)


print('6. Convertir la lista anterior a tupla y:')
canciones = tuple(canciones)
print('La lista canciones convertida a tupla:',canciones)     



#No es posible eliminar un solo elemento de la tupla solamente eliminar la tupla completa utilizando del
'''####a. Eliminar el tercer elemento de la lista ordenada de manera ascendente
del canciones[2]
print('eliminar el tercer elemento de la lista:', canciones)

####b. Eliminar el primer elemento de la lista descendente
del canciones[0]
print('eliminar el primer elemento de la lista:', canciones)'''