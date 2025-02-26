def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Devuelve la posición del valor encontrado
    return None  # Si no se encuentra, devuelve None

# Definimos la matriz 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Solicitamos al usuario un número a buscar
valor_buscar = int(input("Ingrese el número a buscar: "))

# Buscamos el valor en la matriz
posicion = buscar_valor(matriz, valor_buscar)

# Mostramos el resultado
if posicion:
    print(f"El número {valor_buscar} se encuentra en la posición {posicion}.")
else:
    print(f"El número {valor_buscar} no se encontró en la matriz.")