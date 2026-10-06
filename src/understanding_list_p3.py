# Trabajando con listas
print("\n\ Aqui aprendere a trabajar con listas\n".upper())
# lista de puros trings
foods = ["cookie","soda","fries","burrito","cake"]
print(foods) 

#voy a imprimir la lista a la mala
print(foods[0],foods[1],foods[2],foods[3],foods[4])

#voy a imprimir la lista , recorrer una lista con for
print("imprimir con for")
for food in foods:
    print(food)
 #voy a imprimir la lista , recorrer una lista con for con end   
  
for food in foods:
    print(food, end=" ")
print("  ")

# a esto se le llama looping
# for cat in cats
# for dog in dogs

# foods = ["cookie","soda","fries","burrito","cake"]
# imprimir mensaje para cada comida
for food in foods:
    print(f"{food.title()}ese fue un gran festin")
    print(f"ya no quiero ser comida{food.title()}")
print("ni modo")    

# identacion

"""
python utiliza la identacion para determinar cuando
la linea de un cadigo esta conectada a la linea de 
codigo anterior
basicamete, se utilizan 4 espacios en blanco para
 obligarnos a escribir codigo ordenado y estructurado
"""
# no olvidemos identar o sera un identation error
foods =["cookie,soda,fries"]
# for food in foods:
# print(food)# identationerror

# error de logica
foods =["cookie","soda","fries"]
for food in foods:
    print(food)
print(f"no puedo esperar para dejar de ser comida")# como no tiene identacion solo sera un mensaje al final

# identacion inecesaria
message = "hello pyyy"
# print(message) 

# no olvidar los dos puntos
#for food in foods
#   print(food)
