# Variables en Python

first_name = 'Alejandra'
last_name = 'Mora'
country = 'Mexico'
city = 'Zacatecas'
age = 25
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Alejandra', 
    'lastname':'Mora', 
    'country':'Mexico',
    'city':'Zacatecas'
    }

# Imprimir los valores almacenados en las variables

print('Nombre:', first_name)
print('Longitud del nombre:', len(first_name))
print('Apellido: ', last_name)
print('Longitud del apellido: ', len(last_name))
print('Pais: ', country)
print('Ciudad: ', city)
print('Edad: ', age)
print('Habilidades: ', skills)
print('Información personal: ', person_info)

# Declarar múltiples variables en una línea

first_name, last_name, country, age = 'Alejandra', 'Mora', 'Mexico', 25

print(first_name, last_name, country, age)
print('Nombre:', first_name)
print('Mora: ', last_name)
print('México: ', country)
print('Edad: ', age)
