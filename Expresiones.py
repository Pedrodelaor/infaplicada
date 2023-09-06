#2 ejemplos de expresiones Aritméticas
print('2 ejemplos de expresiones Aritmeticas')
print('ejemplo #1 de expresion aritmetica')

print('SUMA')
a= 23
print('a=',a)
b= 33 
print('b=',b)
c= a+b
print('c=a+b',c)
print('la suma de a+b=',c)

print('ejemplo #2 de expresion aritmetica')

print('MULTIPLICACION')
d= 14
print('d=',d)
e= 31 
print('e=',e)
f= d*e
print('f=d*e',f)
print('la multiplicacion de d*e=',f)



#2 ejemplos de expresiones Relacionales  
print('2 ejemplos de expresiones Relacionales')
print('ejemplo #1 de expresion relacional')

print('Mayor o igual que (>=)')
g= 56
print('g=',g)
h= 29 
print('h=',h)
j= g>=h
print('j= g>=h',j)
print('la relacion de j= g>=h ES:',j)

print('ejemplo #2 de expresion relacional')

print('Menor o igual que (<=)')
k= 78
print('k=',k)
l= 52 
print('l=',l)
m= k<=l
print('m= k<=l',m)
print('la relacion de m= k<=l ES:',m)

#2 ejemplos de expresiones Lógicas
print('2ejemplos de expresiones Logicas')
print('ejemplo #1 de expresion logica')

print('Operador AND')
n= 3==3 and 7>6
print('operador AND de 4-1==3 and 7>6 ES:',n)

print('ejemplo #2 de expresion logica')

print('Operador OR')
r= 4==3 or 3>6
print('operador OR de  4==3 or 3>6  ES:',r)


#1 ejemplo de expresión de Carácter
print('1 ejemplo de expresiones de Carácter')

import re

texto = "Hoy es el día 25 del mes"
patron = '[0-9]+'  # Expresión regular para encontrar números

numeros_encontrados = re.findall(patron, texto)
print('Números encontrados:', numeros_encontrados)
