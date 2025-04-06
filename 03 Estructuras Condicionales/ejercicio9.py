magnitud = float(input("Por favor, ingresa la magnitud del terremoto según la escala de Richter: "))

if magnitud < 3:
    clasificacion = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    clasificacion = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    clasificacion = "Muy Fuerte (puede causar daños significativos)"
else:
    clasificacion = "Extremo (puede causar graves daños a gran escala)"
    print(f"La magnitud {magnitud} en la escala de Richter corresponde a: {clasificacion}")