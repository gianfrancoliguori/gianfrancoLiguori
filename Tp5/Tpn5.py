import functions
#EJERCICIO 1


"""
document_num = input("Ingrese su numero de documento: ")
if ( functions.document(document_num)):
    print("la longitud es correcta")
else:
    print("longitud incorrecta")
"""


"""
#EJERCICIO 2


# Main
text = input("INGRESE FRASE: ")
result = functions.word_len(text)
print("La longitud de la última palabra es:", result)
"""

#EJERCICIO 3
"""
# Programa principal
partners = []

while True:
    complete_name = input("Ingrese el nombre completo del socio (o nombre vacío para salir): ").strip()

    if not complete_name:
        break

    dni = input("Ingrese el número de DNI del socio: ").strip()

    while not functions.validate_dni(dni):
        print("El número de DNI ingresado no es válido. Debe tener 7 u 8 dígitos.")
        dni = input("Ingrese el número de DNI del socio: ").strip()

    parts_name = complete_name.split()
    first_name = parts_name[0]
    surname = parts_name[-1]

    # Generar el identificador único
    identifier = functions.generate_identifier(first_name, surname, dni)
    partners.append(identifier)


print("\nIdentificadores únicos de los socios:")
for identifier in partners:
    print(f"ID -> {identifier}")


"""


#EJERCICIO 4

"""


number_one = int(input("Ingrese el primer número entero: "))
number_two = int(input("Ingrese el segundo número entero: "))

if functions.multiple(number_one, number_two):
    print(f"{number_one} es múltiplo de {number_two}")
elif functions.multiple(number_two, number_one):
    print(f"{number_two} es múltiplo de {number_one}")
else:
    print("Ninguno de los números es múltiplo del otro")
"""

"""
#EJERCICIO 5
    
days = int(input("de cuantos dias desea saber la temperatura media"))

for day in range(days):
    min_tem = int(input("Cual es la temperatura minima?: "))
    max_tem = int(input("Cual es la temperatura maxima?: "))
    print("la temperatura media es ",functions.temperature_middle(min_tem, max_tem),"º")

"""

"""
#EJERCICIO 6

sentence = input("INGRESE FRASE: ")
print("la frase separada es ",functions.separator(sentence))

"""

"""
#EJERCICIO 7

# Programa principal
numbers = []

while True:
    answer = input("Ingrese un número o escriba 'fin' para terminar: ")
    
    if answer.lower() == 'fin':
        break
    
    try:
        number = float(answer)
        numbers.append(number)
    except ValueError:
        print("Entrada no válida. Intente de nuevo.")

maximum, minimum = functions.max_and_min(numbers)

if maximum is not None and minimum is not None:
    print(f"El valor máximo es: {maximum}")
    print(f"El valor mínimo es: {minimum}")
else:
    print("No se ingresaron números para encontrar el máximo y el mínimo.")
"""

"""
#EJERCICIO 8

# Programa principal
try:
    radio = float(input("Ingrese el radio de la circunferencia: "))
    if radio < 0:
        print("El radio no puede ser negativo.")
    else:
        area, perimeter = functions.area_and_perimeter(radio)
        print(f"Área de la circunferencia: {area}")
        print(f"Perímetro de la circunferencia: {perimeter}")
except ValueError:
    print("Entrada no válida. Ingrese un número válido para el radio.")
"""

#EJERCICIO 9
"""

# Programa principal
tries = 0
max_tries = 3

while tries < max_tries:
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    access_allowed, tries = functions.login(username, password, tries)

    if access_allowed:
        print("Acceso concedido. Bienvenido, usuario1.")
        break
    else:
        print("Acceso denegado. Nombre de usuario o contraseña incorrectos.")
        if tries < max_tries:
            print(f"Le quedan {max_tries - tries} intentos restantes.")
        else:
            print("Se han agotado los intentos. Cierre el programa.")

if tries >= max_tries:
    print("Se han agotado los intentos de inicio de sesión.")
"""
#EJERCICIO 10

"""
cart = {
    "product1": 50,
    "product2": 30,
    "product3": 20
}

discounts = {
    "product1": 10,
    "product3": 15
}

price_final = functions.apply_discounts(cart, discounts)
print(f"Precio final con descuento: {price_final}")



"""
"""
#EJERCICIO 11


numbers = [4,2,8,9,6]

print("-- primer lista --")
for number in numbers:
    print(number)

new_numbers = function.apply_function(function.product, numbers) 
print("-- segunda lista --")
for number in new_numbers:
    print(number)
"""

"""
#EJERCICIO 12

phrase = input("Ingrese una frase: ")
words = phrase.split(" ")

keys = (functions.define_keys(words))
print(functions.transform_dict(words))
"""
"""
#EJERCICIO 13
vector = (3, 4, 5)  
module = functions.module_vector(vector)
print(f"El módulo del vector {vector} es {module}")
"""
"""
#EJERCICIO 14
num=int(input("Ingrese un numero: "))
if functions.es_primo(num) == True:
    print(num,"es un numero primo")
else:
    print(num,"no es un numero primo")

"""

"""
#EJERCICIO 15
cont=0
while True:
    number=int(input("Ingrese un numero (0 para salir): "))
    cont+=1
    if number == 0:
        print("Has ingresado",cont-1,"numeros")
        break
    else:
        fact5=functions.factorial(number)
        print("El factorial de",number,"es:",fact5)
"""

#EJERCICIO 16

try:
    number = int(input("Ingrese un número entero: "))
    digit = int(input("Ingrese un dígito para contar su frecuencia: "))
    
    if 0 <= digit <= 9:
        frequency = functions.frequency_function(number, digit)
        print(f"El dígito {digit} aparece {frequency} veces en el número {number}.")
    else:
        print("El dígito ingresado no es válido (debe estar entre 0 y 9).")
except ValueError:
    print("Entrada no válida. Ingrese un número entero y un dígito válido.")

#EJERCICIO 17
higher_primo = None
factorial = 1

while True:
    try:
        number = int(input("Ingrese un número primo (o un número no primo para salir): "))
        
        if number <= 0:
            print("El número debe ser mayor que 0.")
            continue

        if not functions.is_primo(number):
            break

        if number > higher_primo:
            higher_primo = number

        sum_digits = sum_digits(number)
        print(f"Suma de los dígitos: {sum_digits}")

        digit = int(input("Ingrese un dígito para contar su frecuencia: "))
        frequency = functions.calculate_frequency(number, digit)
        print(f"Frecuencia del dígito {digit}: {frequency}")

    except ValueError:
        print("Entrada no válida. Ingrese un número entero válido.")

if higher_primo is not None:
    for i in range(1, higher_primo + 1):
        factorial *= i

    print(f"Factorial del mayor número primo ingresado ({higher_primo}): {factorial}")
else:
    print("No se ingresaron números primos.")









