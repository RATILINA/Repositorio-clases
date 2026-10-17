# Ejercicio

age = input("\ningresa tu edad:")
print(age)
#print(type(age))
age = int(age)
#print(type(age))
#if age <= 4:
    cost = 0

#if age > 4 and age < 18 :
    cost = 200

#if age >= 18:
    cost = 0

print(f"el costo de tu boleto es: {cost}")

# bloque if-elif-else

#if age <= 4:
    cost = 0
#elif age > 4 and age < 18 :
    cost = 200
#elif age >= 18:
    cost = 0
#else :
    cost = 0

print("bloque if-elif-else")
print(f"el costo de tu boleto es: {cost}")


if age <= 4:
    cost = 0
elif age > 4 and age < 18 :
    cost = 200
elif age >= 18 and age < 65:
    cost = 500
elif age >= 65:
    cost = 0


