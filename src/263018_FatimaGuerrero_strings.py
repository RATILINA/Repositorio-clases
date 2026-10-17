#Fatima Guerrero Morales
#2630018
#grupo 1

#Resumen ejecutivo
"""
un string es un tipo de dato inmutable que nos permite guardar texto
como nombres o palabras "fatima", se pueden cocatenar para uniser o 
se pueden contar con len, se puede usar slicing para partirlos,
podemis usar strip para eliminar espacios o lower para minusculas,
validar y normalizar nos ayuda a evitar errores, en este docuento
se encontraran diferentes problemas usando los strings, junto con
3 tipos de casos
"""

# PROBLEMA 1 Full name formatter (name + initials)
"""
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).
"""
"""
Inputs: nombre completo
Outputs: nombre separado, iniciales de nombre
Validations: si el nombre completo tiene menos de dos palabras
#Test cases:
1) Normal: nombre de 3 o mas palabras
2) Border: nombre de 2 palabras
3) Error: nombre de menos de 2 palabras
"""

full_name = input("Enter your full name: ").strip() # I use `input` to enter the name and `strip` to remove spaces.

if not full_name:
    print("Error: invalid input") # If nothing is entered, mark it as an error.

name_parts = full_name.split() # split to divide the string

if len(name_parts) < 2: # Use `len` if the number of words is less than two.
    print("Error: enter at least two words") 

formatted_name = full_name.title() # Capitalize the first letter of each word using title case.

initials = name_parts[0][0].upper() + "." + name_parts[1][0].upper() + "." + name_parts[2][0].upper() + "."
print("Formatted name:", formatted_name)
print("Initials:", initials)


# PROBLEMA 2 Simple email validator (structure + domain)
"""
Valida si una dirección de correo tiene un formato básico correcto:
- Contiene exactamente un '@'.
- Después del '@' debe haber al menos un '.'.
- No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio (la parte después de '@').
"""
"""
Inputs:email
Outputs:dominio
Validations: si ingresamos un email, si hay @ y si hay un "." despues de @
#Test cases:
1) Normal:email normal
2) Border: email sin punto
3) Error: email con doble @
"""

email_text = input("Enter your email: ").strip() # input field for entering an email address

if not email_text:
    print("Error: enter your email")

elif email_text.count("@") != 1: # elif to check that there is an @ symbol 
    print("Error: invalid email")

elif " " in email_text: # and that it is not followed by an absence of a period
    print("Error: invalid email")

else:
    at_position = email_text.find("@") # find to locate @
    domain_part = email_text[at_position + 1:]

    if "." not in domain_part:
        print("Error: invalid email")
    else:
        print("Valid email: true")
        print("Domain:", domain_part)


# PROBLEMA 3 Palindrome checker (ignoring spaces and case)
"""
Determina si una frase es un palíndromo,
es decir, se lee igual de izquierda a derecha
y de derecha a izquierda, ignorando espacios
y mayúsculas/minúsculas.
"""
"""
Inputs:frase
Outputs:si es palindromo true y si no es false
Validations:si es palindromo
#Test cases:
1) Normal:un palindromi
2) Border:una frase normal
3) Error:no poner nada
"""

phrase = input("Enter your phrase:") # input for entering text

if not phrase:
    print("Error: not valid")

cleaned_phrase = phrase.replace(" ","").lower() # replace the spaces with non-spaces

if len(cleaned_phrase) <3: # that the phrase has no fewer than 3 characteres
    print("Error: input must contain at least 3 characters") 

reversed_phrase = cleaned_phrase[::-1] # Reverse the sentence by index using -1

if cleaned_phrase == reversed_phrase:
    print("Is palindrome: true")
elif cleaned_phrase != reversed_phrase:
    print("Is palindrome: false")



# PROBLEMA 4  Sentence word stats (lengths and first/last word)

"""
Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).
"""
"""
Inputs:la oracion
Outputs:oracion separada,numero de palabras, la palabra mas larga y la mas corta
Validations:si la oracion esta vacia
#Test cases:
1) Normal:una oracion de mas de 1 palabra "hola py como tas"
2) Border: una palabra "hola"
3) Error:no escribir nada
"""

sentence = input("Enter your sentence:").strip()

if not sentence :
    print("Error:not valid")

word_list = sentence.split() # split to separate the sentence
print(word_list)

word_count = len(word_list) # Read to count how many words are in the sentence
print("word count:",word_count)

first_word= word_list[0] # first word
last_word = word_list[-1] # last word

print("First word:", first_word)
print("Last word:", last_word)

shortest_word = min(word_list, key=len) # key=len to apply the function to each one
longest_word = max(word_list, key=len)

print("Shortest word:", shortest_word)
print("Longest word:", longest_word)


# PROBLEMA 5 Password strength classifier
"""
Clasifica una contraseña como "weak", "medium" o "strong"
 según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).
Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).
"""
"""
Inputs:letras o caracteres o numeros
Outputs:nivel de seguridad
Validations:la contrasea no debe esta vacia,longitud,si tiene caracteres 
#Test cases:
1) Normal: Ertyuio3! 
2) Border: Ertyuio3
3) Error: no poner nada
"""

password_input = input("Enter a password: ").strip()  

if not password_input:  # Here, I check if the password is empty.
    print("Error: invalid input")  # Here I show an error message if the password is empty.

else:
    has_upper = False  # Here I create a variable to check if the password 
    has_lower = False  
    has_digit = False  
    has_symbol = False 

    for character in password_input:  # Here i check each character in the password
        if character.isupper():  # Here i check if the character is uppercase
            has_upper = True
        elif character.islower():  # Here i check if the character is lowercase
            has_lower = True
        elif character.isdigit():  # Here i check if the character is a number
            has_digit = True
        else:
            has_symbol = True  # Here, I mark that the password contains a symbol

    if len(password_input) < 8:  # Here, I check if the password has fewer than 8 characters
        strength = "weak"  # Here, I classify short passwords as weak
    elif has_upper and has_lower and has_digit and has_symbol:  # Here I check if the password has all four types of characters
        strength = "strong"  # Here, I classify the password as strong
    else:
        strength = "medium"  # Here I classify passwords that do not meet the strong rules as medium

    print("Password strength:", strength)  # Here I display the final password classification


# PROBLEMA 6 
"""
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres
"""
"""
Inputs:nombre de producto, precio de producto
Outputs:etiqueta
Validations:que no se ingresen textos vacios
#Test cases:
1) Normal:orange,5
2) Border:soap,23.43
3) Error:no poner nada
"""
product_name = input("Enter the product name:").strip()

if not product_name:
    print("Error:not valid")

product_price = input("Enter the product price:").strip()
product_value = float(product_price)

if product_value <= 0:
    print("Error: not valid")
else:
        label = f"Product: {product_name} | Price: ${product_value:.2f}"  # Here i create the product label

        if len(label) < 30:  # Here i check if the label has fewer than 30 characters
                label = label + " " * (30 - len(label))  # Here iadd spaces to reach 30 characters
        else:
                label = label[:30]  # Here ikeep only the first 30 characters

        print("Label:", label)  
        print("Length:", len(label))  # Here i check the label length

# Conclusion
"""
los strings son muy importantes y yo diria que la base de varias cosasc,
funcionan para mosrar texto, indicaciones, lsitas, tuplas y mas, strip 
me ayudo para porder eliminar espacios que al momento de probar el codigo
pudieramos poner, lower para las minusculas, split para separar palabras 
y crear las listas que utilice, normalizar el texto nos ayuda a no tener 
errores con posibles respuestas por ejemplo
"""
# Referencias
"""
-Repositorio clases
-Repositorio charly
-https://programminghistorian.org/es/lecciones/normalizar-datos
-https://www.ionos.mx/digitalguide/paginas-web/desarrollo-web/python-split/
-https://thedataschools.com/python/strings/title-metodo-string.html
-https://ellibrodepython.com/mutabilidad-python

"""