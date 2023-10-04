import math
#1
def document(dni) :
    if (len(dni)>=7 and len(dni)<=8):
        dni_correct = True
    else:
        dni_correct = False
    return dni_correct


#2
def word_len(s):
    # Elimina los espacios en blanco al principio y al final del string
    s = s.strip()
    
    # Divide el string en palabras utilizando los espacios en blanco como separadores
    word = s.split()
    
    # Verifica si hay palabras
    if len(word) > 0:
        # Toma la última palabra de la lista
        last_word = word[-1]
        
        # Calcula la longitud de la última palabra
        large = len(last_word)
        
        return large
    else:
        # Si no hay palabras, retorna 0
        return 0


#3
def validate_dni(dni):
    return len(dni) == 7 or len(dni) == 8 and dni.isdigit()

def generate_identifier(name, surname, dni):
    first_name = name.split()[0]
    surname_letters = len(surname)
    first_3_digits = dni[:3]
    identifier = f"{first_name}{surname_letters}{first_3_digits}"
    return identifier


#4
def multiple(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

#5   
def temperature_middle(min_temperature, max_temperature):
    med_temperature = (min_temperature + max_temperature)/2
    return med_temperature

#6
def separator(sentence):
    item=" "
    sentence_separate = item.join(sentence)
    return sentence_separate

#7
def max_and_min(numbers):
    if len(numbers) == 0:
        return None, None  
    maximum = numbers[0] 
    minimum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    return maximum, minimum


#8
def area_and_perimeter(radio):
    
    area = 3.14 * radio**2
    
    perimeter = 2 * 3.14 * radio
    
    return area, perimeter


#9
def login(user, contraseña, intentos):
    
    if user == "usuario1" and contraseña == "asdasd":
        return True, intentos
    else:
        intentos += 1
        return False, intentos 

#10
def apply_discounts(cart, discounts):
    price_total = 0

    for product, price in cart.items():
        if product in discounts:
            discount = discounts[product]
            price_discount = price - (price * discount / 100)
            price_total += price_discount
        else:
            price_total += price

    return price_total


#11
def product(element):
    return element * 2

def apply_function(product, numbers):
    result = []
    for number in numbers:
        result.append(product(number))
    return result

#12
def define_keys(all_keys):
    for sing_key in all_keys:
        list_keys = [sing_key]
    return(all_keys)

def transform_dict(all_words):
    dict_text = {}
    for word in all_words:
        dict_text [word] = len(word)
    return(dict_text)

#13
def module_vector(vector):
    x, y, z = vector
    module = math.sqrt(x**2 + y**2 + z**2)
    return module

#14
def is_primo(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
        else:
            return True


#15
def factorial(n):
    if n==0 or n==1:
            result=1
    elif n>1:
            result=n*factorial(n-1)
    return result

#16
def frequency_function(number, digit):
    counter = 0
    while number > 0:
        digit_actual = number % 10
        if digit_actual == digit:
            counter += 1
        number //= 10  # Eliminamos el último dígito del número
    return counter

#17
def is_primo(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum

def calculate_frequency(number, digit):
    counter = 0
    while number > 0:
        digit_actual = number % 10
        if digit_actual == digit:
            counter += 1
        number //= 10
    return counter

