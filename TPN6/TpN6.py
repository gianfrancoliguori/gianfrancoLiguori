"""
#EJERCICIO 1

numbers = []

while True:
    # Solicita al usuario que ingrese un número
    answer = input("Ingresa un número (0 para finalizar): ")

    # Intenta convertir la entrada a un número entero
    try:
        number = int(answer)
    except ValueError:
        print("¡Ingresa un número válido!")
        continue

    # Si el número es 0, sale del bucle
    if number == 0:
        break

    # Agrega el número a la lista
    numbers.append(number)

# Muestra la lista de números ingresados
print("Números ingresados:", numbers)




#EJERCICIO 2

# Inicializa una lista con algunos números de ejemplo
numbers = [1, 2, 3, 4, 5]

while True:
    # Solicita al usuario que ingrese un número
    answer = input("Ingresa un número para eliminar (0 para salir): ")

    # Intenta convertir la entrada a un número entero
    try:
        number = int(answer)
    except ValueError:
        print("¡Ingresa un número válido!")
        continue

    # Si el número es 0, sal del bucle
    if number == 0:
        break

    # Busca el número en la lista
    if number in numbers:
        # Elimina la primera ocurrencia del número en la lista
        numbers.remove(number)
        print(f"Se eliminó la primera ocurrencia de {number} en la lista.")
    else:
        print(f"{number} no está en la lista. No se puede eliminar.")

# Muestra la lista actualizada
print("Lista actualizada:", numbers)



#EJERCICIO 3

# Inicializa una lista con algunos números de ejemplo
numbers = [1, 2, 3, 4, 5]

# Inicializa una variable para almacenar la suma
sum = 0

# Itera a través de la lista y suma los números
for number in numbers:
    sum += number

# Imprime la suma total
print("La suma de los números en la lista es:", sum)





#EJERCICIO 4
# Crear una lista de números de ejemplo
numbers = [1, 2, 3, 4, 5]

# Solicitar al usuario que ingrese un número
max_number = int(input("Ingresa un número: "))

# Crear una nueva lista con números menores que el número dado
minor_numbers = []

# Iterar a través de los números originales y agregarlos a la nueva lista si son menores
for number in numbers:
    if number < max_number:
        minor_numbers.append(number)

# Imprimir la nueva lista
print("Números menores que", max_number, "son:", minor_numbers)




#EJERCICIO 5

# Crear una lista de números de ejemplo
numbers = [5, 16, 2, 5, 57, 5, 2]

# Crear un diccionario para almacenar las ocurrencias de cada número
occurrences = {}

# Llenar el diccionario con las ocurrencias
for number in numbers:
    if number in occurrences:
        occurrences[number] += 1
    else:
        occurrences[number] = 1

# Crear una lista de tuplas a partir del diccionario
new_list = list(occurrences.items())

# Imprimir la nueva lista de tuplas
print(new_list)





#EJERCICIO 6
# Crear listas para almacenar los nombres de los alumnos de nivel primario y secundario
primary_students = []
secondary_students = []

# Solicitar los nombres de los alumnos de nivel primario
print("Ingresa los nombres de los alumnos de nivel primario (ingresa 'x' para finalizar):")
while True:
    name = input()
    if name == 'x':
        break
    primary_students.append(name)

# Solicitar los nombres de los alumnos de nivel secundario
print("Ingresa los nombres de los alumnos de nivel secundario (ingresa 'x' para finalizar):")
while True:
    name = input()
    if name == 'x':
        break
    secondary_students.append(name)

# a. Informar los nombres de todos los alumnos sin repeticiones
all_students = list(primary_students + secondary_students)
print("Nombres de todos los alumnos sin repeticiones:", all_students)

# b. Informar los nombres que se repiten entre los alumnos
repeated_names = []
for name in primary_students:
    if name in secondary_students and name not in repeated_names:
        repeated_names.append(name)
print("Nombres que se repiten entre los alumnos de nivel primario y secundario:", repeated_names)

# c. Informar los nombres de nivel primario que no se repiten en nivel secundario
primary_names_not_repeat = []
for name in primary_students:
    if name not in secondary_students and name not in primary_names_not_repeat:
        primary_names_not_repeat.append(name)
print("Nombres de nivel primario que no se repiten en nivel secundario:", primary_names_not_repeat)




#EJERCICIO 7

# Inicializar un diccionario para contar las ocurrencias de caracteres
occurrences = {}

# Contador para llevar un registro de la cantidad de strings procesados
counter_strings = 0

# Procesar strings hasta que se hayan ingresado 50
while counter_strings < 50:
    string = input("Ingresa un string (o presiona Enter para finalizar): ")

    # Verificar si se presionó Enter para finalizar la entrada
    if not string:
        break

    # Contar las ocurrencias de cada carácter en el string
    for char in string:
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1

    # Incrementar el contador de strings
    counter_strings += 1

# Mostrar las ocurrencias de cada carácter
print("Ocurrencias de caracteres:")
for char, quantity in occurrences.items():
    print(f"'{char}': {quantity}")


#EJERCICIO 8
# Crear una matriz para los goles, donde goles[i][j] representa los goles del equipo i contra el equipo j.
numbers_teams = 10
scores = [[0 for _ in range(numbers_teams)] for _ in range(numbers_teams)]

# Leer los resultados de los partidos (simulado en este ejemplo)
results = [
    (1, 2, 2, 1), (1, 3, 1, 1), (1, 4, 2, 2), (1, 5, 3, 0), (1, 6, 1, 1), (1, 7, 2, 1), (1, 8, 2, 1), (1, 9, 2, 0), (1, 10, 3, 1),
    (2, 3, 1, 0), (2, 4, 2, 1), (2, 5, 0, 1), (2, 6, 0, 2), (2, 7, 1, 2), (2, 8, 2, 2), (2, 9, 0, 1), (2, 10, 1, 3),
    (3, 4, 1, 1), (3, 5, 1, 2), (3, 6, 0, 1), (3, 7, 0, 2), (3, 8, 1, 0), (3, 9, 2, 2), (3, 10, 2, 3),
    (4, 5, 1, 2), (4, 6, 1, 2), (4, 7, 2, 3), (4, 8, 1, 1), (4, 9, 0, 1), (4, 10, 1, 1),
    (5, 6, 0, 1), (5, 7, 2, 1), (5, 8, 1, 2), (5, 9, 1, 1), (5, 10, 1, 3),
    (6, 7, 1, 2), (6, 8, 2, 1), (6, 9, 0, 2), (6, 10, 0, 2),
    (7, 8, 0, 1), (7, 9, 2, 2), (7, 10, 1, 2),
    (8, 9, 1, 0), (8, 10, 2, 1),
    (9, 10, 0, 3)
]

# Inicializar listas para llevar un registro de triunfos, empates, derrotas, goles a favor y goles en contra de cada equipo.
wins = [0] * numbers_teams
ties = [0] * numbers_teams
defeats = [0] * numbers_teams
goals_for = [0] * numbers_teams
goals_against = [0] * numbers_teams

# Calcular los resultados para cada equipo
for result in results:
    teamA, teamB, scoreA, scoreB = result
    scores[teamA - 1][teamB - 1] = scoreA
    scores[teamB - 1][teamA - 1] = scoreB

    if scoreA > scoreB:
        wins[teamA - 1] += 1
        defeats[teamB - 1] += 1
    elif scoreA < scoreB:
        wins[teamB - 1] += 1
        defeats[teamA - 1] += 1
    else:
        ties[teamA - 1] += 1
        ties[teamB - 1] += 1

    goals_for[teamA - 1] += scoreA
    goals_for[teamB - 1] += scoreB
    goals_against[teamA - 1] += scoreB
    goals_against[teamB - 1] += scoreA

# Calcular la diferencia de goles y puntos para cada equipo
goal_difference = [gf - gc for gf, gc in zip(goals_for, goals_against)]
points = [3 * t + e for t, e in zip(wins, ties)]

# Mostrar los resultados
for team in range(numbers_teams):
    print(f"Equipo {team + 1}:")
    print(f"Triunfos: {wins[team]}, Empates: {ties[team]}, Derrotas: {defeats[team]}")
    print(f"Goles a favor: {goals_for[team]}, Goles en contra: {goals_against[team]}")
    print(f"Diferencia de goles: {goal_difference[team]}")
    print(f"Puntos: {points[team]}\n")


#EJERCICIO 9
import random

# Crear una matriz para el tablero de juego
def make_board(row, column):
    number = list(range(1, (row * column // 2) + 1))
    random.shuffle(number)
    board = [[0] * column for _ in range(row)]
    for i in range(row):
        for j in range(column):
            board[i][j] = number.pop()
    return board

# Imprimir el tablero actual (mostrar cartas visibles)
def print_board(board, cards_showed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i, j) in cards_showed:
                print(f'{board[i][j]:2}', end=' ')
            else:
                print('##', end=' ')
        print()

# Voltear una carta (mostrar su valor)
def down_cart(row, column, board, show_cards):
    show_cards.append((row, column))
    print_board(board, show_cards)
    if len(show_cards) == 2:
        if board[show_cards[0][0]][show_cards[0][1]] == board[show_cards[1][0]][show_cards[1][1]]:
            print("¡Encontraste una pareja!")
            show_cards.clear()
        else:
            print("No es una pareja. Inténtalo de nuevo.")
            show_cards.pop()
            show_cards.pop()

# Verificar si el juego ha terminado (todas las cartas encontradas)
def finish_game(board, show_cards):
    all_cards = set((i, j) for i in range(len(board)) for j in range(len(board[0])))
    return all_cards == set(show_cards)

# Función principal del juego
def play_memory(rows, columns):
    board = make_board(rows, columns)
    cards_showed = []
    tries = 0

    print("¡Bienvenido al juego de Memoria!")
    while not finish_game(board, cards_showed):
        print("\nTablero actual:")
        print_board(board, cards_showed)
        try:
            row = int(input("Ingresa la fila de la carta que deseas voltear: ")) - 1
            column = int(input("Ingresa la columna de la carta que deseas voltear: ")) - 1
            if 0 <= row < rows and 0 <= column < columns and (row, column) not in cards_showed:
                down_cart(row, column, board, cards_showed)
                tries += 1
            else:
                print("Ubicación no válida. Inténtalo de nuevo.")
        except (ValueError, IndexError):
            print("Ingresa una ubicación válida.")

    print("¡Felicidades! Has encontrado todas las parejas en", tries, "intentos.")

# Ejecutar el juego
if __name__ == "__main__":
    rows = 4  # Número de filas del tablero
    columns = 4  # Número de columnas del tablero
    play_memory(rows, columns)


#EJERCICIO 10

# Función para obtener la diagonal principal e inversa de una matriz cuadrada
def make_diagonal(arr):
    dimension = len(arr)
    
    # Inicializar listas para la diagonal principal y la diagonal inversa
    diagonal_principal = []
    diagonal_reverse = []
    
    # Recorrer la matriz para obtener los elementos de las diagonales
    for i in range(dimension):
        diagonal_principal.append(arr[i][i])  # Elementos de la diagonal principal
        diagonal_reverse.append(arr[i][dimension - 1 - i])  # Elementos de la diagonal inversa
    
    return diagonal_principal, diagonal_reverse

# Ejemplo de uso
square_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_principal, diagonal_reverse = make_diagonal(square_array)

print("Diagonal Principal:", diagonal_principal)
print("Diagonal Inversa:", diagonal_reverse)


#EJERCICIO 11

# Crear el diccionario de divisas y símbolos
money_dictionary = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

# Solicitar al usuario que ingrese una divisa
money = input("Ingresa una divisa (Euro, Dollar o Yen): ")

# Buscar la divisa en el diccionario y mostrar su símbolo o un mensaje de aviso
if money in money_dictionary:
    symbol = money_dictionary[money]
    print(f"El símbolo de {money} es {symbol}")
else:
    print("La divisa ingresada no está en el diccionario.")


#EJERCICIO 12

# Solicitar al usuario que ingrese su nombre, edad, dirección y teléfono
name = input("Ingresa tu nombre: ")
age = input("Ingresa tu edad: ")
address = input("Ingresa tu dirección: ")
phone = input("Ingresa tu número de teléfono: ")

# Crear un diccionario con la información proporcionada por el usuario
user_info = {
    'name': name,
    'age': age,
    'address': address,
    'phone': phone
}

# Mostrar la información del usuario
msg = f"{user_info['name']} tiene {user_info['age']} años, vive en {user_info['address']} y su número de teléfono es {user_info['phone']}."
print(msg)

"""

#EJERCICIO 13

# Crear un diccionario con los precios de las frutas
fruit_prices = {
    'manzana': 1.0,
    'banana': 0.5,
    'naranja': 0.75,
    'pera': 1.2,
    'uva': 2.0
}

# Solicitar al usuario que ingrese el nombre de una fruta y la cantidad en kilos
fruit = input("Ingresa el nombre de la fruta: ").lower()  # Convertir a minúsculas para ser insensible a mayúsculas/minúsculas
kilos = float(input("Ingresa la cantidad en kilos: "))

# Buscar la fruta en el diccionario y calcular el precio
if fruit in fruit_prices:
    total_price = fruit_prices[fruit] * kilos
    print(f"El precio de {kilos} kilos de {fruit} es ${total_price:.2f}")
else:
    print("Lo siento, la fruta no está en la lista de precios.")




















