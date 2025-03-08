
#INGREASR UNA FRASE Y CONTAR LAS VOCALES:

vowels = ['a', 'e', 'i', 'o', 'u']
frase = input("Ingresa una frase: ").lower() 
vocales_encontradas = [letra for letra in frase if letra in vowels]
print(f"Cantidad de vocales: {len(vocales_encontradas)}")
print(f"Vocales encontradas: {vocales_encontradas}")
