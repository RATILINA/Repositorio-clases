# Fatima Guerrero Morales
# 2630018
# grupo 1

# resumen
"""
en este trabajo aprendere a usar datos como int o float, int
para numeros enteros y float para numeros decimales o flotantes, 
los booleanos son o tue o false, y toman decisiones, como un prendido
o apagado, las validaciones nos ayudan a detectar datos incorrectos y evitarlos
"""
# PROBLEMA 1 Temperature converter and range flag
"""
Convierte una temperatura en grados Celsius (float) a Fahrenheit
y Kelvin. Además, determina un valor booleano is_high_temperature
que sea true si la temperatura en Celsius es mayor o igual que 
30.0 y false en caso contrario.
"""
"""
Inputs: temperatura celsius
Outputs:Temperatura en Fahrenheit y Kelvin
Validations:true o false
Test cases:
1) Normal:25°C
2) Border:30°C
3) Error:-300°C
"""

# Constants
MIN_KELVIN = 0.0
#Input
temp_c = float(input("Enter temperature in Celsius: "))#We use float because temperatures aren't always whole numbers and can have decimals

# Arithmetic operations to make the conversions to Fahrenheit and Kelvin
temp_f = temp_c * 9 / 5 + 32 # multiply, divide, and add
temp_k = temp_c + 273.15 # add

is_valid_range = temp_k >= MIN_KELVIN #preventing physically impossible Kelvin temperatures < 0.0

is_high_temperature = temp_c >= 30 #boolean value that is
#true if the temperature in Celsius is greater than or equal to 30.0 

#Outputs
print("Results:")
print("Fahrenheit:", temp_f)
print("Kelvin:", temp_k)
print("High temperature:", is_high_temperature) #True or False

# PROBLEMA 2  Work hours and overtime payment
"""
Calcula el pago total semanal de un trabajador. 
Hasta 40 horas se pagan a hourly_rate (float). 
Las horas extra (> 40) se pagan al 150% de la
tarifa normal. Además, genera un booleano has_overtime
que indique si el trabajador hizo horas extra
"""
"""
Inputs:Horas traajadas y pago por horas
Outputs:Pago regular, horas extra, pago total y booleano de horas extra
Validations:Horas mayores o iguales a 0 y pago por hora mayor a 0
Test cases:
1) Normal:35 horas y $100 por hora
2) Border:40 horas y $100 por hora
3) Error: -5 horas
"""

HOURLY_RATE = 180.0 # Fixed hourly rate constant
#Inputs
hours_worked = float(input("Enter hours worked: ")) # We use float because hours can have decimals

if hours_worked >= 0 and HOURLY_RATE > 0:# Check if hours are positive and rate is greater than zero with AND
    regular_hours = min(hours_worked, 40)#regular hours
    overtime_hours = max(0.0, hours_worked - 40) # Get overtime 
#3 cases:
    regular_pay = regular_hours * HOURLY_RATE # Calculate regular pay
    overtime_pay = overtime_hours * HOURLY_RATE * 1.5 #Calculate overtime pay at 150%
    total_pay = regular_pay + overtime_pay # Calculate total weekly pay

    has_overtime = hours_worked > 40 ## Boolean value that is true if there are overtime hours
#Outputs
    print("Regular pay:", regular_pay)
    print("Overtime pay:", overtime_pay)
    print("Total pay:", total_pay)
    print("Has overtime:", has_overtime) # True or False
else:
    print("Error: invalid input") #Error


# PROBLEMA 3 Discount eligibility with booleans
"""
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible
"""
"""
Inputs:tal de compra (float), estudiante y adulto mayor yes o not
Outputs:Elegibilidad, descuento y precio final
Validations:Compra mayor o igual a 0 y respuestas válidas
Test cases:
1) Normal:Compra de $500, estudiante YES
2) Border:Compra de $1000, ambas respuestas NO
3) Error:Compra de -$100
"""

purchase_total = float(input("Enter purchase total: ")) # We use float for currency values
is_student_text = input("Is student (YES/NO): ").upper() #uppercase
is_senior_text = input("Is senior (YES/NO): ").upper() #uppercase

# 'or' valida que sea "YES" o "NO"; 'and' exige que TODAS las condiciones sean verdaderas para continuar. #Needs all 3 true
if purchase_total >= 0.0 and (is_student_text == "YES" or is_student_text == "NO") and (is_senior_text == "YES" or is_senior_text == "NO"):
    is_student = is_student_text == "YES" # Convert student text to boolean (TRUE/FALSE)
    is_senior = is_senior_text == "YES" # Convert senior text to boolean (TRUE/FALSE)

#OR: It's enough for just one of the three options to be true for discount_eligible to be True
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0) # Check if eligible for discount

    if discount_eligible:
        final_total = purchase_total * 0.9 # Apply 10% discount #The operation gives you 90% of the original price of what you'll pay
    else:
        final_total = purchase_total # Keep original total

    print("Discount eligible:", discount_eligible) # True or False
    print("Final total:", final_total)
else:
    print("Error: invalid input") #texto no es “SÍ” ni “NO”


# PROBLEMA 4 Basic statistics of three integers
"""
Lee tres números enteros y calcula: suma, promedio (float)
, valor máximo, valor mínimo y un booleano all_even que indique 
si los tres números son pares.
"""
"""
Inputs:Tres números enteros (int)
Outputs:Suma, promedio, máximo, mínimo y booleano para saber si todos son pares
Validations:Los tres valores deben ser números enteros válidos
Test cases:
1) Normal:2, 4, 6
2) Border:0, 0, 0
3) Error:2, "pyy", 6
"""

n1 = int(input("Enter first integer: ")) # Convert input (string) to integer with int
n2 = int(input("Enter second integer: ")) 
n3 = int(input("Enter third integer: ")) 

sum_value = n1 + n2 + n3 # Calculate total sum
average_value = sum_value / 3 # Calculate average as float
max_value = max(n1, n2, n3) # Get maximum value
min_value = min(n1, n2, n3) # Get minimum value
all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0) # Check if all three numbers are even

#Outputs
print("Sum:", sum_value) #sum
print("Average:", average_value) #average
print("Maximum value:", max_value) #Maximum value
print("Minimum value:", min_value) #Minimum value
print("All even:", all_even) # True or False


# PROBLEMA 5 Loan eligibility (income and debt ratio)
"""
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650
"""
"""
Inputs:Ingreso mensual (float), deuda mensual (float) y puntaje crediticio (int)
Outputs:Porcentaje de deuda y booleano de elegibilidad
Validations:Ingreso mayor a 0, deuda mayor o igual a 0 y puntaje válido
Test cases:
1) Normal:Ingreso 10000, deuda 2000, puntaje 700
2) Border:Ingreso 8000, deuda 3200, puntaje 650
3) Error:Ingreso 0
"""

monthly_income = float(input("Enter monthly income: ")) # Read monthly income as float(string)
monthly_debt = float(input("Enter monthly debt: ")) # Read monthly debt as float(string)
credit_score = int(input("Enter credit score: ")) # Read credit score as integer

# Validate inputs to avoid division by zero and negative values using logical operators
#the three values must be true
if monthly_income > 0.0 and monthly_debt >= 0.0 and credit_score >= 0:
    # Calculate debt ratio
    debt_ratio = monthly_debt / monthly_income

    # Determine loan eligibility using logical operators
    #the three values must be true
    eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)

    # Outputs
    print("Debt ratio:", debt_ratio)
    print("Eligible:", eligible) # True or False
else:
    print("Error: invalid input")


# PROBLEMA 6 Body Mass Index (BMI) and category flag
"""
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)
"""
"""
Inputs:Peso en kilogramos y altura en metros (float)
Outputs:IMC y booleanos para clasificar el resultado
Validations:Peso y altura mayores a 0
Test cases:
1) Normal:Peso 70 kg, altura 2 m
2) Border:Peso 74 kg, altura 2 m
3) Error: Altura 0
"""

#Input
weight_kg = float(input("Enter weight in kg: ")) # Read weight in kilograms. They’re not always whole numbers, sometimes they’re decimals
height_m = float(input("Enter height in meters: ")) # Read height in meters. They’re not always whole numbers, sometimes they’re decimals

# Validate inputs to ensure positive values and avoid division by zero
#the two values must be true because is an AND
if weight_kg > 0.0 and height_m > 0.0:
    # Calculate BMI (Body Mass Index) 
    bmi = weight_kg / (height_m * height_m)#Use operations suggested by the teacher
    rounded_bmi = round(bmi, 2) #round a value to the number of decimals
    ##In this case: Using round(bmi, 2) to show 2 decimals

    # Determine category flags
    is_underweight = bmi < 18.5 #BMI less than 18.5
    is_normal = (bmi >= 18.5) and (bmi < 25.0)#the two values must be true because is an AND
    is_overweight = bmi >= 25.0 #BMI over 25

    # Outputs
    print("#Results:")
    print("BMI:", rounded_bmi)
    print("Underweight:", is_underweight)
    print("Normal:", is_normal)
    print("Overweight:", is_overweight)
else:
    print("Error: invalid input")


# 8. CONCLUSIONS
"""
Aprendí a utilizar int y float según el tipo de dato que necesito por
ejemplo 4 como int y float como 4.5 y Comprendí cómo los booleanos True
y False ayudan a tomar decisiones aprendí a realizar operaciones matemáticas
y comparar diferentes valores las validaciones son importantes para evitar 
errores con datos incorrectos también comprendí la importancia de comprobar
que un divisor no sea cero utilizar variables con nombres claros facilita 
la lectura y comprensión del código
"""
"""
Referencias:
-repositorio clases
- repositorio charly
-https://recursospython.com/guias-y-manuales/booleanos-operaciones-logicas-y-binarias/#google_vignette
-https://ellibrodepython.com/entero-en-python
-https://ellibrodepython.com/operadores-aritmeticos
"""