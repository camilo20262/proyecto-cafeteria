# pedidos.py
ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\nElige el café que prefieras")
    print("1. Cappuccino")
    print("2. Americano")
    print("3. Té")
    print("4. Expreso")

    cafes = {
        "1": "cappuccino",
        "2": "americano",
        "3": "té",
        "4": "expreso"
    }

    opcion = input("Elige un café que prefieras: ")

    if opcion in cafes:  # valida contra las keys
        cafe_elegido = cafes[opcion]
        print("Has pedido un " + cafe_elegido + ". Preparando tu café...")

        # escritura en modo append con UTF-8
        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")

    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
