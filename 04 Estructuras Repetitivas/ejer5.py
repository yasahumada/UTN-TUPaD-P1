import random

# Generar número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0

print("¡Adivina el número entre 0 y 9!")

while True:
    intento = int(input("Ingresa tu número: "))
    intentos += 1

    if intento == numero_secreto:
        print(f" ¡Correcto! El número era {numero_secreto}.")
        print(f" Lo adivinaste en {intentos} intento(s).")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")