def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento y lo retorna.
    :param monto_total: Total de la compra
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (10% por defecto)
    :return: Monto del descuento calculado
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
total_compra1 = 1000
descuento1 = calcular_descuento(total_compra1)
monto_final1 = total_compra1 - descuento1

print(f"Compra 1: Total: ${total_compra1}, Descuento: ${descuento1}, Monto final: ${monto_final1}")

# Segunda llamada con un porcentaje de descuento diferente
total_compra2 = 1500
descuento2 = calcular_descuento(total_compra2, 15)
monto_final2 = total_compra2 - descuento2

print(f"Compra 2: Total: ${total_compra2}, Descuento: ${descuento2}, Monto final: ${monto_final2}")
