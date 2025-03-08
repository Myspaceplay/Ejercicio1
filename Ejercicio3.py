# Cadena original
frase = "El mejor regalo? El perdón..."

# Convertir la cadena en una lista de caracteres
list_frase = list(frase)

# Eliminar signos de puntuación usando métodos de listas
list_frase = [car for car in list_frase if car not in ["?", "."]]

# Convertir "El" en "el" modificando directamente la lista
list_frase[0] = list_frase[0].lower()

# Reconstruir la frase sin los signos de puntuación
nueva_frase = ''.join(list_frase).strip() + "."

# Mostrar resultados
print("Lista de caracteres procesada:", list_frase)
print("Nueva frase:", nueva_frase)
