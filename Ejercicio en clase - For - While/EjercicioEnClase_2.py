numero = int(input("Ingresa un número (0 para terminar): "))
total_pares = 0
total_impares = 0

while numero != 0:
    num = numero  
    pares = 0
    impares = 0
    
    while num > 0:
        digito = num % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        num //= 10
    
    total_pares += pares
    total_impares += impares
    
    print(f"El número {numero} tiene {pares} dígitos pares y {impares} dígitos impares.")
    
    numero = int(input("Ingresa un número (0 para terminar): "))

print("Total de dígitos pares:", total_pares)
print("Total de dígitos impares:", total_impares)
