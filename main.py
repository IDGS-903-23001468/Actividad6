from operaciones import calcular_descuento, calcular_iva, precio_con_iva


def calcular_total(precio, descuento):
    precio_descuento = calcular_descuento(precio, descuento)
    total = precio_con_iva(precio_descuento)
    return total


def main():
    try:
        precio = float(input("Ingresa el precio: "))
        descuento = float(input("Ingresa el descuento: "))

        total = calcular_total(precio, descuento)

        print("Total a pagar:", total)

    except ValueError:
        print("Error: Ingresa solamente números.")


if __name__ == "__main__":
    main()