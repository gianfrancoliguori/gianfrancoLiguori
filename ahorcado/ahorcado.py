import random

# Lista de palabras a adivinar
words = ["messi", "otamendi", "paredes", "molina", "alvarez", "dimaria"]

# Función para seleccionar una palabra al azar
def select_word():
    return random.choice(words)

# Función para mostrar el estado actual de la palabra a adivinar
def show_word(word, guessed_letter):
    result = ""
    for letter in word:
        if letter in guessed_letter:
            result += letter
        else:
            result += "_"
    return result

# Función principal del juego
def play_ahorcado():
    tries_max = 6
    word_to_guess = select_word()
    letter_guessed = []
    tries = 0

    print("¡Bienvenido al juego del ahorcado!")
    print(show_word(word_to_guess, letter_guessed))

    while True:
        letter = input("Adivina una letra: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Ingresa una sola letra válida.")
            continue

        if letter in letter_guessed:
            print("Ya has adivinado esta letra.")
            continue

        letter_guessed.append(letter)

        if letter not in word_to_guess:
            tries += 1
            print(f"Letra incorrecta, te quedan {tries_max - tries} intentos.")
            if tries >= tries_max:
                print("¡Perdiste! La palabra correcta era:", word_to_guess)
                break
        else:
            word_now = show_word(word_to_guess, letter_guessed)
            print("Adivinaste una letra correctamente:", letter)
            print(word_now)
            if word_now == word_to_guess:
                print("¡Ganaste! Has adivinado la palabra.")
                break

if __name__ == "__main__":
    play_ahorcado()
