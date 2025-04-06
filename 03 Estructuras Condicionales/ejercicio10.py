hemisferio = input("¿En qué hemisferio te encuentras? (N para hemisferio norte, S para hemisferio sur): ").strip().upper()
mes = int(input("Ingresa el número del mes (1-12): "))
dia = int(input("Ingresa el día del mes (1-31): "))

# Función para determinar la estación del año en el hemisferio norte
def estacion_norte(mes, dia):
    if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 3) or (mes == 3 and dia <= 20):
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (mes >= 4 and mes <= 6) or (mes == 6 and dia <= 20):
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (mes >= 7 and mes <= 9) or (mes == 9 and dia <= 20):
        return "Verano"
    else:  # Otoño
        return "Otoño"

# Función para determinar la estación del año en el hemisferio sur
def estacion_sur(mes, dia):
    if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 3) or (mes == 3 and dia <= 20):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (mes >= 4 and mes <= 6) or (mes == 6 and dia <= 20):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (mes >= 7 and mes <= 9) or (mes == 9 and dia <= 20):
        return "Invierno"
    else:  # Primavera
        return "Primavera"

# Determinar la estación según el hemisferio
if hemisferio == "N":
    estacion = estacion_norte(mes, dia)
elif hemisferio == "S":
    estacion = estacion_sur(mes, dia)
else:
    estacion = "Hemisferio no válido"

# Imprimir el resultado
print(f"En el hemisferio {hemisferio}, el día {dia} del mes {mes} corresponde a la estación: {estacion}")