"""
Las listas nos ppermiten almacenar informacion en un lugar
, la cantidad que se desee ya sean pocos

una lista es una coleccin de items (elementos)que tienen un orden particular
se pueden crear listas que inckuyan strings, enteros, floats, los nombres de 
las personas de tu familia, etc, podemos almacenar (los tipos de datos)


ejemplo,, 
"""
bicycles = ['trek', 'cannolate', 'redline']
print(bicycles)

"""
las listas son colecciones ordenadas, se puede accder a un elemento de una lista
diciendole a python la posicion o indice del elemento deseado

para obtener el valor deseado, se debe escribir el nombre de la lista seguido de el indice del elemento entre corchetes


"""

print([bicycles[0], bicycles[1], bicycles[2]])
print(bicycles[0].upper())

"""
los indices comientzan en  no en 1,

"""
print(bicycles[1]) # cannolate
print(bicycles[2]) # redline

"""
accediendo al ultimo elemento de una lista
"""
print(bicycles[-1])
print(bicycles[-2])

""" 
utilizando valores individuales de unba lista

"""
message  = f"my first bicycle was a (bicycles[-1].upper())"
print(message)
