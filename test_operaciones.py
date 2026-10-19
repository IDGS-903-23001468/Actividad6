from operaciones import calcular_descuento, calcular_iva, precio_con_iva

def test_descuento():
    assert calcular_descuento(100, 10) == 90

def test_iva():
    assert calcular_iva(100) == 16

def test_precio_con_iva():
    assert precio_con_iva(100) == 116