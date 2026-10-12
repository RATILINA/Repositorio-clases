"""
 las tuplas son listas que no puedo modificar,
listas que no cambian de tamaño
se utilizan () para definir una tupla
ejemplo:
si tenemos u rectangulo (largo,ancho) que siempre va a tener el 
mismo tamañp, podemos asegurar que sus dimensiones no van a
cambiar, si colocamos sus valores
"""
dimensions = (200,50)
print("tupla original:", dimensions)

#vamos a imprimir una tupla
print(dimensions[0])
print(dimensions[1])
print(dir(dimensions))

"""
en las lsitas si se puede modificar los valores de sus indices
pero en las tuplas no se puede
names = ["carlos","charly","juan"]


"""
""" se ppuede re definir la variables"""
dimensions = (200,100,300)
print("tupla re de finida", dimensions)


#tipos de datos boleanos
answer = True
print(answer)
#print(dir(answer))