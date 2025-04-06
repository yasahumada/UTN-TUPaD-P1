nombre = input("Por favor, ingresa tu nombre: ")

# Solicitar la opción de transformación
print("Elige una opción para transformar tu nombre:")
print("1. En mayúsculas.")
print("2. En minúsculas.")
print("3. Con la primera letra mayúscula.")
opcion = input("Ingresa 1, 2 o 3: ")

# Transformar el nombre según la opción seleccionada
if opcion == '1':
    nombre_transformado = nombre.upper()  # Convierte el nombre a mayúsculas
elif opcion == '2':
    nombre_transformado = nombre.lower()  # Convierte el nombre a minúsculas
elif opcion == '3':
    nombre_transformado = nombre.capitalize()  # Convierte la primera letra a mayúscula
else:
    nombre_transformado = "Opción no válida"  # En caso de que se ingrese una opción inválida

# Imprimir el resultado
print("Resultado:", nombre_transformado)