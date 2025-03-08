
#PARA GENERAR EL ABECEDARIO:

def generar_abecedario():
    #Genera el abecedario en español, incluyendo la 'ñ'.
    abecedario = [chr(letra) for letra in range(ord('a'), ord('z') + 1)]
    abecedario.insert(14, 'ñ')  # Insertar la 'ñ' en la posición correcta
    return abecedario

def filtrar_abecedario(abecedario, x):
    #Filtra las letras en posiciones que sean múltiplos de x.
    return [letra for i, letra in enumerate(abecedario, start=1) if i % x != 0]

# Ejecutar funciones
abecedario = generar_abecedario()
print("Abecedario completo:")
print(abecedario)

# Definir valor de x
x = 3  # Puedes cambiar este valor según necesidad

# Filtrar y mostrar
abecedario_filtrado = filtrar_abecedario(abecedario, x)
print(f"\nAbecedario filtrado (sin posiciones múltiplos de {x}):")
print(abecedario_filtrado)
