# -------- DICCIONARIOS --------
print("\n=== DICCIONARIOS ===")
informacion_personal = {
    "nombre": "Juan Perez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}
print("Diccionario original:", informacion_personal)

# Modificar "ciudad"
informacion_personal["ciudad"] = "Barcelona"
print("Después de modificar 'ciudad':", informacion_personal)

# Verificar si "telefono" existe, si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-789"
print("Después de verificar/agregar 'telefono':", informacion_personal)

# Eliminar clave "edad"
del informacion_personal["edad"]
print("Después de eliminar 'edad':", informacion_personal)

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
