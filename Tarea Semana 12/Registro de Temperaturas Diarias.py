import random

# Definir dimensiones de la matriz
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Se pueden agregar más semanas si es necesario

# Crear una matriz 3D para almacenar las temperaturas
matriz_temperaturas = [[[random.randint(15, 35) for _ in dias_semana] for _ in range(semanas)] for _ in ciudades]

# Calcular y mostrar los promedios de temperatura por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nTemperaturas para {ciudad}:")
    for j in range(semanas):
        promedio = sum(matriz_temperaturas[i][j]) / len(dias_semana)
        print(f"  Semana {j + 1}: Promedio de temperatura = {promedio:.2f}°C")