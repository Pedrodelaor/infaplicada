###1. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, manzana, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "Ibm", "Oracle", "Amazon"] 

###2. Print the list using _print()_
print('Compañías de it:', it_companies)

###3. Print the number of companies in the list
print("Número de las compañías:", len(it_companies))

###4. Print the first, middle and last company
primera_compañía = it_companies[0]
print('La primera compañía es:', primera_compañía)
compañía_de_enmedio = it_companies[len(it_companies)//2]
print('La compañía de enmedio es:', compañía_de_enmedio)
ultima_compañía = it_companies[-1]
print('La última compañía es:', ultima_compañía)

###5. Print the list after modifying one of the companies
it_companies[0] = 'Instagram'
print('La lista modificada es:', it_companies)

###6. Add an IT company to it_companies
it_companies.append("SpaceX")
print('La lista con una compañía añadida es:', it_companies)

###7. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Linkedin")
print('La lista de las compañías con una más agregada enmedio:', it_companies)

###8. Change one of the it_companies names to uppercase (Microsoft excluded!)
for i in range(len(it_companies)):
    if it_companies[i] != "Microsoft":
        it_companies[i] = it_companies[i].upper()
print('La lista de las compañías en letras mayúsculas a excepción de Microsoft que se mantiene igual:', it_companies)

###9. Join the it_companies with a string '#;&nbsp; '
joined_companies = '#;&nbsp; '.join(it_companies)
print('Lista de compañías unidas por ;&nbsp:', joined_companies)

###10. Check if a certain company exists in the it_companies list.
Existe = 'Google' in it_companies
Existe2 = 'GOOGLE' in it_companies
print('¿En la lista existe el nombre Google?:', Existe)
print('¿En la lista existe el nombre GOOGLE?', Existe2)