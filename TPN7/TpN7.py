#EJERCICIO 1

"""
def bubbleSort(numbers):
  for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
      if numbers[j] > numbers[j + 1]:
        temp = numbers[j]
        numbers[j] = numbers[j+1]
        numbers[j+1] = temp
        


numbers = []
n = 5
while n>0:
    number = int(input("ingrese numero: "))
    numbers.append(number)
    n -= 1

print("LISTA")
print(numbers)
print("LISTA ORDENADA")
bubbleSort(numbers)
print(numbers)
"""

#EJERCICIO 2

"""
def sort_selection(word_list):
    n = len(word_list)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if word_list[j] < word_list[min_idx]:
                min_idx = j
        word_list[i], word_list[min_idx] = word_list[min_idx], word_list[i]

# Solicitar al usuario que ingrese una lista de palabras separadas por espacios
answer = input("Ingresa una lista de palabras separadas por espacios: ")
words = answer.split()

# Llamar a la función de ordenamiento de selección
sort_selection(words)

# Mostrar la lista ordenada
print("Lista ordenada alfabéticamente:")
print(" ".join(words))
"""

#EJERCICIO 3

"""
# Crear una lista de diccionarios con información de libros
books = [
    {'titulo': 'Libro A', 'autor': 'Autor X', 'año_publicacion': 2005},
    {'titulo': 'Libro B', 'autor': 'Autor Y', 'año_publicacion': 2010},
    {'titulo': 'Libro C', 'autor': 'Autor Z', 'año_publicacion': 2000},
    {'titulo': 'Libro D', 'autor': 'Autor X', 'año_publicacion': 2015},
]

# Función para ordenar la lista de libros utilizando el método de ordenamiento de selección
def sort_selection(book_list, camp):
    n = len(book_list)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if book_list[j][camp] < book_list[min_idx][camp]:
                min_idx = j
        book_list[i], book_list[min_idx] = book_list[min_idx], book_list[i]

# Solicitar al usuario que ingrese el campo por el cual desea ordenar
camp = input("Ingrese el campo por el cual desea ordenar (titulo, autor, año_publicacion): ")

# Verificar si el campo es válido
if camp not in books[0]:
    print("El campo ingresado no es válido.")
else:
    # Llamar a la función para ordenar la lista de libros
    sort_selection(books, camp)
    
    # Mostrar la lista de libros ordenada
    print("Lista de libros ordenada por", camp)
    for book in books:
        print(f"Título: {book['titulo']}, Autor: {book['autor']}, Año de Publicación: {book['año_publicacion']}")


"""

#EJERCICIO 4

"""
def insertion_sort_by_length(chains_list):
    n = len(chains_list)
    for i in range(1, n):
        word_actual = chains_list[i]
        j = i - 1
        while j >= 0 and len(word_actual) < len(chains_list[j]):
            chains_list[j + 1] = chains_list[j]
            j -= 1
        chains_list[j + 1] = word_actual

# Solicitar al usuario que ingrese una lista de cadenas separadas por espacios
answer = input("Ingresa una lista de cadenas separadas por espacios: ")
chains = answer.split()

# Llamar a la función de ordenamiento de inserción por longitud
insertion_sort_by_length(chains)

# Mostrar la lista de cadenas ordenada por longitud
print("Lista de cadenas ordenada por longitud:")
print(" ".join(chains))
"""

#EJERCICIO 5

"""
books = [
    {'titulo': 'Libro A', 'autor': 'Autor X', 'año_publicacion': 2005},
    {'titulo': 'Libro B', 'autor': 'Autor Y', 'año_publicacion': 2010},
    {'titulo': 'Libro C', 'autor': 'Autor Z', 'año_publicacion': 2000},
    {'titulo': 'Libro D', 'autor': 'Autor X', 'año_publicacion': 2015},
]

def descending_selection_sort(book_list, camp):
    n = len(book_list)
    
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if book_list[j][camp] > book_list[max_idx][camp]:
                max_idx = j
        book_list[i], book_list[max_idx] = book_list[max_idx], book_list[i]

# Solicitar al usuario que ingrese el campo por el cual desea ordenar
camp = input("Ingrese el campo por el cual desea ordenar (titulo, autor, año_publicacion): ")

# Verificar si el campo es válido
if camp not in books[0]:
    print("El campo ingresado no es válido.")
else:
    # Llamar a la función para ordenar la lista de libros en orden descendente
    descending_selection_sort(books, camp)
    
    # Mostrar la lista de libros ordenada en orden descendente
    print("Lista de libros ordenada en orden descendente por", camp)
    for book in books:
        print(f"Título: {book['titulo']}, Autor: {book['autor']}, Año de Publicación: {book['año_publicacion']}")


"""

#EJERCICIO 6

"""
def order_for_count(numbers_list):
    if not numbers_list:
        return []

    # Encontrar el valor máximo en la lista
    max_value = max(numbers_list)

    # Inicializar una lista de conteo con ceros para cada valor posible
    count = [0] * (max_value + 1)

    # Contar la frecuencia de cada número en la lista
    for num in numbers_list:
        count[num] += 1

    # Reconstruir la lista ordenada
    list_order = []
    for i in range(max_value + 1):
        list_order.extend([i] * count[i])

    return list_order

# Solicitar al usuario que ingrese una lista de números enteros separados por espacios
answer = input("Ingresa una lista de números enteros separados por espacios: ")
numbers = list(map(int, answer.split()))

# Llamar a la función de ordenamiento por conteo
list_order = order_for_count(numbers)

# Mostrar la lista ordenada
print("Lista de números ordenada por ordenamiento por conteo:")
print(" ".join(map(str, list_order)))
"""

#EJERCICIO 7

"""
def numbers_order(number_list):
    n = len(number_list)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]



mix_list = [5, 'manzana', 2, 'banana', 10, 'pera', 'naranja']
numbers = []
str_list = []

for element in mix_list:
    if isinstance(element, (int, float)):
        numbers.append(element)
    elif isinstance(element, str):
        str_list.append(element)


numbers_order(numbers)
str_list.sort()

mix_list_order = numbers + str_list

print(mix_list_order)
"""

#EJERCICIO 8

def merge_sort(numbers):
    if len(numbers) > 1:
        middle = len(numbers) // 2
        middle_left = numbers[:middle]
        middle_right = numbers[middle:]

        merge_sort(middle_left)
        merge_sort(middle_right)

        i = j = k = 0

        while i < len(middle_left) and j < len(middle_right):
            if middle_left[i] < middle_right[j]:
                numbers[k] = middle_left[i]
                i += 1
            else:
                numbers[k] = middle_right[j]
                j += 1
            k += 1

        while i < len(middle_left):
            numbers[k] = middle_left[i]
            i += 1
            k += 1

        while j < len(middle_right):
            numbers[k] = middle_right[j]
            j += 1
            k += 1

def merge_sort_ejemplo():
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", numbers)
    merge_sort(numbers)
    print("Lista ordenada:", numbers)

merge_sort_ejemplo()





