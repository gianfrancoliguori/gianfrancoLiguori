corrimiento = int(input("Ingresa el corrimiento: "))
mensajes = []

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(5):
    mensaje = input("Ingresa el mensaje: ")
    mensaje_encriptado = ""
    
    for letra in mensaje:
        if letra.isalpha():
            es_mayuscula = letra.isupper()
            letra = letra.lower()
            indice = (alfabeto.index(letra) + corrimiento) % 26
            nueva_letra = alfabeto[indice]
            if es_mayuscula:
                nueva_letra = nueva_letra.upper()
            mensaje_encriptado += nueva_letra
        else:
            mensaje_encriptado += letra
    
    mensajes.append(mensaje_encriptado)

print("Mensajes encriptados:")
for mensaje in mensajes:
    print(mensaje)
