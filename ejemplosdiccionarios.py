cosas_universidad= {'alumnos':['Daniel','Pedro','Luis','Nancy','Fer'], 
                    'utiles': ['mochila','pluma', 'cuaderno','computadora'],
                    'inmuebles':['edificio','salon','biblioteca','estadio','laboratorios']
                   }

print('Estos son las listas de los diccionarios:',cosas_universidad)
print('Esta es la longitud de los diccionarios:',len(cosas_universidad))
print('Estas es la lista del diccionario de inmuebles:',cosas_universidad['inmuebles'])
print('Hay bares en la universidad?:',cosas_universidad.get('bares'))

del cosas_universidad['utiles']
print('Esta es la lista con el diccionario utiles eliminado:', cosas_universidad)

llaves = cosas_universidad.keys()
print('Esas son las llaves del diccionario:', llaves)
valores = cosas_universidad.values()
print('Estos son los valores de los diccionarios:', valores)
