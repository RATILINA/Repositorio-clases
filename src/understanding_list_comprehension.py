"""
es para crear listas en una sola line sin tener que hacer mucho

"""
squares = [value**2 for value in range(1,11)]
print(squares)

#agregar algo antes de cada miembro de la lista
names = ["fatilina","alexis", "piter"]
names_upv = [name + "  kick  " for name in names]
print(names_upv)


names = ["fatilina","alexis", "piter","La chicharra" ]
names_upv = [name + "  kick  " for name in names]
print(names_upv)



