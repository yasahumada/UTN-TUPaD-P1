CANTIDAD_NUMEROS = 100

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Introduce {CANTIDAD_NUMEROS} números enteros:")

for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Número {i+1}: "))

    # Contar pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Contar positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")