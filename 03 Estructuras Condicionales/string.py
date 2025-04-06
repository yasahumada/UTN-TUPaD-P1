entrada = input("Por favor, ingrese una palabra o frase: ")
if entrada[-1].lower() in 'aeiou':
    entrada += '!' 
print(entrada)