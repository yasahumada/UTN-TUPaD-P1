# Solicita al usuario un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Verifica que el número sea positivo
if numero < 0:
    print("Por favor, introduce un número entero **positivo**.")
else:
    # Calcula la suma desde 0 hasta el número ingresado (incluido)
    suma = sum(range(numero + 1))
    print(f"La suma de los números desde 0 hasta {numero} es: {suma}")