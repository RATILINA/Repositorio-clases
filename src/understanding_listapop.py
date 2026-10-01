# lista pop
"""
la lista .pop() sirve para eliminar elementos por indice
no borra toda la lista ojoo
si no se le ppone nada entre parentesis al pop se borrara el
ultimo elemento, pero si se le pone indice se borrara ese

"""
print("\n\ Aqui aprendi a utilizar el metodo pop".title())
motorcycles_4 = ["honda", "suzuki", "hd", "mortalica"]
print(motorcycles_4 )
deleted_motorcycle = motorcycles_4. pop()
print(f"tu motocicleta borrada es : {deleted_motorcycle}") # con f strings
print("tu motocicleta borrada es", deleted_motorcycle ) # antes de que existieran los f strings
print(motorcycles_4 )
print("\n\ Aqui aprendi a utilizar el metodo pop con indice".title())
motorcycles_4 = ["honda", "suzuki", "hd", "mortalica"]
print(motorcycles_4 )
deleted_motorcycle = motorcycles_4. pop(2)
print(f"tu motocicleta borrada es : {deleted_motorcycle}") # con f strings
print(motorcycles_4 )


