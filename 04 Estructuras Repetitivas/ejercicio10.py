# Solicita al usuario un número
numero = input("Introduce un número entero: ")

# Verifica si es negativo
if numero.startswith('-'):
    # Invertimos sin el signo y luego lo volvemos a agregar
    numero_invertido = '-' + numero[:0:-1]
else:
    numero_invertido = numero[::-1]

# Mostrar el número invertido
print(f"El número invertido es: {numero_invertido}")