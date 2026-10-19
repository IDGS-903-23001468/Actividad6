def calcular_descuento(precio, descuento):
    return precio - (precio * (descuento / 100))

def calcular_iva(precio):
    return precio * 0.16

def precio_con_iva(precio):
    return precio + calcular_iva(precio)