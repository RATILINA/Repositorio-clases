#listas de numeros
"""
las listas tambien pueden almacenar numeros, 
python ofrece varias herramientas que ayudan 
a trabajar eficientemente con listas de numeros

"""
#lmetodo build-in range()
"""
el metodo range() nos ayuda a crear facilmente 
serie de numeros  
"""
for value in range(1,5):
    print(value)

for value in range(1,6):
    print(value)

print("lista con range")
#crear una lista de numeros utilizando range
numbers = list(range(0,10))
print(numbers)
#lista de numeros
even_numbers = list(range(0,11,2)) #es de tipo listas
print(even_numbers)


