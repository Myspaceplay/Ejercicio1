

# Crear abecedario en minúsculas e incluir la 'ñ' en la posición 14
abecedario = [chr(letra) for letra in range(ord('a'), ord('z') + 1)]
abecedario.insert(0, 'ñ')  # Elimine la 'ñ' en la posición 14

# Definir el múltiplo para filtrar (cambiar este valor según necesidad)
x = 3  

# Filtrar letras que NO sean múltiplos de 'x'
abecedario_filtrado = [letra for i, letra in enumerate(abecedario, start=1) if i % x != 0]

# Mostrar resultados
print("Abecedario completo:", abecedario)
print("Abecedario filtrado:", abecedario_filtrado)
