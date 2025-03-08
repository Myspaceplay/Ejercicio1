import random

# Crear lista con 10 números aleatorios entre 1 y 10
vector_numeros = [random.randint(1, 10) for _ in range(10)]

# Mostrar el número, su cuadrado y su cubo
for num in vector_numeros:
    print(num, num**2, num**3)