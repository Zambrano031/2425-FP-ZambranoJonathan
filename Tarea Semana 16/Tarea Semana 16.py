# Trabajo con Archivos de Texto en Python

# ----------------------------
# Escritura de Archivo de Texto
# ----------------------------

# Definimos el nombre del archivo
nombre_archivo = "my_notes.txt"

# Abrimos el archivo en modo escritura ("w")
# Si el archivo no existe, se crea automáticamente
archivo = open(nombre_archivo, "w")

# Escribimos al menos tres líneas de notas personales
archivo.write("Nota 1: Hoy aprendí a trabajar con archivos en Python.\n")
archivo.write("Nota 2: Los métodos write() y readline() son muy útiles.\n")
archivo.write("Nota 3: Recuerda siempre cerrar el archivo después de usarlo.\n")

# Cerramos el archivo después de escribir
archivo.close()

# ----------------------------
# Lectura de Archivo de Texto
# ----------------------------

# Abrimos el archivo en modo lectura ("r")
archivo = open(nombre_archivo, "r")

# Leemos el contenido línea por línea usando readline()
print("Contenido del archivo línea por línea:")
linea = archivo.readline()
while linea:
    print(linea.strip())  # Usamos .strip() para eliminar saltos de línea al imprimir
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
