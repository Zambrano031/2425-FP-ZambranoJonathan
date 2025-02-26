def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de elementos

# Definimos la matriz 3x3
matriz = [
    [34, 12, 9],
    [88, 56, 32],
    [77, 41, 25]
]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegimos la fila a ordenar (por ejemplo, la segunda fila, índice 1)
fila_a_ordenar = 1

# Ordenamos la fila seleccionada
bubble_sort(matriz[fila_a_ordenar])

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)