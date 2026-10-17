# Fatima Guerrero Morales 
# 2630018
# grupo 1

"""
Resumen ejecutivo
una lista sirve para guardar varios datos y se escribe con corchetes
una tupla también guarda varios datos, pero se escribe con paréntesis
un diccionario guarda datos mediante claves y valores.
La diferencia es que las listas y tuplas guardan elementos en orden, 
mientras que los diccionarios permiten identificar cada dato por su clave
una lista es mutable porque puedo agregar, eliminar o modificar sus elementos
una tupla es inmutable porque sus elementos no se pueden modificar después de crearla.
Los diccionarios relacionan una clave con un valor, por ejemplo, un nombre con una calificación.
En este documento explicaré cada problema realizado y cómo funciona su solución.
También incluiré las entradas que solicita cada programa y las salidas que muestra.
Explicaré las validaciones utilizadas para evitar errores al ingresar los datos.
"""
# PROBLEMA 1 shopping list basic(list operations)
"""
Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
1) Crear una lista inicial de productos.
2) Permitir agregar un nuevo producto al final.
3) Mostrar la cantidad total de elementos en la lista.
4) Verificar si un producto específico está en la lista (booleano is_in_list).

"""
"""
inputs:["grape", "banana", "lemon", "pozonque"], productos nuevos y producto buscado
outputs:lista inicial y lista nueva, numero total de productos, resultado de busqueda
validation:script(), len(), in
#test cases
normal:agregar un producto valido(chesse, milk o orange),buscar cualquier producto
border:agregar un producto con espacios(  chesse  )
error:No ingresar ningun producto
"""

item_list = ["grape", "banana", "lemon", "pozonque"] # Here I created the list
print(item_list)

new_item = input("\n Enter your new product:").strip()# Here I used an input to add a new product
item_list.append(new_item) # Here the chosen product will be added to the original list
print(item_list)

total_items = len(item_list) # Here len allows us to know how many products we have
print(f"\n You have this number of products:{total_items}")

search_item = input("\n Search for your product:").strip()
is_in_list = search_item in item_list  # The in operator helps us know if the entered element is in our new list
print(f"Product found:{is_in_list}")  


# PROBLEMA 2 Points and distances with tuples
"""
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.

"""
"""
inputs: todos los numeros enteros y flotantes
outputs: todos los numeros designados para a y b, distancia y punto medio de b y a
validation: float()
#test cases
normal:ingresar numeros como 2,3,4,5 para obtener punto medio y distancia
border:ingresar cordenadas iguales 
error:ingresar letras
"""

coordenadas = [] #Here I used an empty list to add the elements of the for loop
for coordenada in ["x1 de a", "y1 de a", "x2 de b", "y2 de b"]: # Use the `for` loop to repeat the input for each value of x or y
    value = float(input(f"Enter the coordinate {coordenada}: ")) # Use float to allow floating-point numbers
    coordenadas.append(value) # Here, I stored the entered data in a list.
   

point_a = (coordenadas[0],coordenadas[1]) # Here I created two tuples with the index
point_b = (coordenadas[2],coordenadas[3])

print(f"Your coordinates for a are:{point_a}")
print(f"Your coordinates for b are:{point_b}")

distance = ((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2 )**0.5 # Here, we use the operations necessary for the distance
print(f"The distance from your coordinate is:{distance}")

midpoint = ((point_a[0] + point_b[0]/2) , (point_a[1] + point_b[1]/2)) # Here, we use the operations necessary for the midpoint
print(f"The midpoint of your coordinate is:{midpoint}")


# PROBLEMA 3:Product catalog with dictionary
"""
Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)

"""
"""
inputs:todas las llaves y los valores 
outputs: producto encontrado, cantidad, cantidad llave y su valor
validation: que el producto exista, que la cantidad sea mayor de cero
#test cases
normal:apple * 3
border:kixi * 1
error: buscar grape
"""

product_prices = {"apple":10.50, "orange":6.50, "banana":11.00, "eggplant":28.40, 
                "carrot":5.30, "potato":5.00, "brocoli":30.00, "strawberry":60.00,"kiwi":50.00}
product_name = input("Enter product name: ").strip()


if product_name in product_prices: # Here, I used an if statement so that if the product is found, it lets us know
     print("Product found")
     quantity = int(input("Enter quantity: "))
     print("valid quantity")
     if quantity > 0:
       print("valid quantity")
       unit_price = product_prices[product_name] # Here, I look up the value in my dictionary based on its key
       total_price = unit_price * quantity # I multiply my product by the quantity.
       total_price = int(total_price) 
     else:
        print("Error: not valid") # If the quantity is not valid, it displays an error.
else:
    print("Error: not found") # If the product is not found, it displays an error.

"""
unit_price = product_prices[product_name] # Here, I look up the value in my dictionary based on its key
total_price = unit_price * quantity # I multiply my product by the quantity.
total_price = int(total_price)
   

quantity = int(input("Enter quantity: ")) # Use int to convert the entered value into an integer.
if quantity > 0: #Check the quantity to ensure it is not less than zero;
    print("valid quantity")
else: 
    print("Error: invalid quantity")# if it is, it must be considered invalid

unit_price = product_prices[product_name] # Here, I look up the value in my dictionary based on its key
total_price = unit_price * quantity # I multiply my product by the quantity.
total_price = int(total_price)

print (total_price)
"""

# PROBLEMA 4: Student grades with dict and list
"""
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.
"""
"""
inputs:nombre de el estudiante
outputs:lista de promedio, si paso o no
validation: si el promedio es mayor o igual que 70, que el nombre exista
#test cases
normal:fatima[90,60], shark[3,70]
border:alexis[70,70]
error:jose 
"""

students_name = ("Fatima", "Renata", "Alexis", "Shark")# I made a list of the students' names.
grade = {"fatima":[90,60], "renata":[90,80], "alexis":[90,67], "shark":[30,70]} # dictionary of students and their grades
print(students_name)

for student,notas in grade.items(): # Here it tells us about the grades stored in 'student' and the marks.
    suma_total= sum(notas)
    promedio = suma_total / len(notas)# use len to find out how many grades there were
    print(f"{student} promedio:{promedio}")

student_name = input("Enter the name: ").strip().lower() # Here, the student is being searched for, and `lower` and `strip` were used to remove spaces.

if student_name in grade: # if the student is found in the grades
    promedio = sum(grade[student_name]) / len(grade[student_name])

    is_passed = promedio >= 70 # If it is greater than or equal to 70, it is true; otherwise, it is false.
    print("Passed:", is_passed)
else:
    print("Error: student not found")

# PROBLEMA 5 Word frequency counter (list + dict)

"""
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.

"""
"""
inputs: cualquier oracion
outputs:diccionario de el numero de palabras repetidas
validation: si la palabra esta repetida osea + de 1 vez
#test cases
normal:cualquier oracion si palabras repetidas
border: oracion conpalabras repetidas
error:nada
"""
sentence = input("Enter a sentence:")
if not sentence.strip():
    print("Error: invalid input")

word_list = sentence.lower().split()
frequencies = {}

for word in word_list:
    if word in frequencies:
            frequencies[word] += 1
    else:
            frequencies[word] = 1

print(frequencies)


# PROBLEMA 6

"""
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.
"""
"""
inputs:acciones, nombres, y numero
outputs:contanto guardado
validation: si no ponen nada marca error
#test cases
normal:add
border:search
error: delete
"""

# Create a dictionary with initial contacts
contacts = {"Fatima": "1234567890","Renata": "0987654321","Charly": "5551234567"}

# Ask the user to enter an action and normalize it
action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

# Check if the action is valid
if action_text not in ("ADD", "SEARCH", "DELETE"):
    print("Error: invalid action")

else:
    # Ask for the contact name
    name = input("Enter contact name: ").strip()

    # Check if the name is empty
    if not name:
        print("Error: invalid input")

    # Add a contact or update an existing one
    elif action_text == "ADD":
        # Ask for the phone number
        phone = input("Enter phone number: ").strip()

        # Check if the phone number is empty
        if not phone:
            print("Error: invalid input")
        else:
            # Save the contact in the dictionary
            contacts[name] = phone
            print("Contact saved:", name, phone)

    # Search for a contact
    elif action_text == "SEARCH":
        # Get the phone number if the contact exists
        phone = contacts.get(name)

        # Display the result

        """
        Conclusion
        gracias a los problemas, aprendi que las listas pueden ser muy utilies, mas cuando se 
        combian con un loop como for o con if que nos permite indagar en la lista, estas funci
        ones tambien se pueden usar en los diccionarios y tuplas pero la diferencia esta en la 
        forma en que podemos usarlos, las listas en mi experiencia se me hacen mas generales,pero
        las tuplas nos pueden ayudar a guardar variables que no queremos que cambie, como un 
        predeterminado, a la misma vez los diccionarios nos permiten asignarle un valor a una 
        variable, y se tratan como llave y clave, esto nos ayuda a usarlas de diferentes maneras
        dependienso si solo queremos valores, o si queremos valores predeterminados para hacer 
        operaciones en base a esos o si queremos, tener una variable con un valor como en el 
        catalogo de productos.
        
        """
        """
        Referencias
        -Repositorio de clases
        -Repositorio de clases de charly
        -https://youtube.com/shorts/y2jVai04778?si=aysUkPG-TZ8zGxm2
        -https://ellibrodepython.com/entero-en-python
        -https://ellibrodepython.com/for-python
        """
        