#solicite al usuario ingresar numeros enteros 
total = 0
print('ingrese numeros enteros uno por uno y 0 para finalizar')
while True:
    numero = int(input("Ingresa un número: "))
    
    if numero == 0:
        break  # Sale del bucle si el número es 0
    
    total += numero  # Suma el número al total

print(f"La suma total es: {total}")
