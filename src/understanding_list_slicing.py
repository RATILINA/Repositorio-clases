players=["fatilina","renata", "mercado", "leo","juan"]
print("lista original:", players)

# slicing
print(players[3:5]) #se ponen los indices # se le agreg uno mas para que aparezcan poreso el 5 y no 4

"""
El slicing me permite trabajar con un grupo
especifico de la lista y al resultado
se le conoce como slice

"""
print("1:4", players[1:4]) 
print(":3", players[:3]) 
print("2:", players[2:]) 
print("-3:", players[-3:]) 

# casos especiales de el slicing
print("casos especiales")
print(players)
print(players[1:10])#me imprime hasta donde puede
print(players[-10:10])#lista vacia
print(players[6:1])#
print(players[0:])#vacio

# looping through slice
print("looping through a slice")
students = ["fatilina","renata", "mercado", "leo","juan"]

# slicing [::]tarea
for student in students:
    print(f"el estudiante:{student}, va a pasar la materia")
print(students)

#como podemos copiar una lista
my_food = ["pizza","tacos", "quesadillas"]

# tres maneras de copiar una lista

# método 1 utilizando slicing

my_friend_food_2 = my_food[:]

# método 2 utilizando el método de las listas.copy()

my_friend_food_3 = my_food.copy()

# método 3 utilizando el método build-in list()

my_friend_food_4 = list(my_food)

