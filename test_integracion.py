from main import calcular_total


def test_total_con_descuento():
    assert calcular_total(100, 10) == 104.4


def test_total_sin_descuento():
    assert calcular_total(100, 0) == 116