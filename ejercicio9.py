compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)