def solicitar_pedido():
    print("\n Elige el cafe que prefieras")
    print("1.Cappuccino")
    print("2.Americano")
    print("3.TE")
    print("4.Expreso")

    opcion=input("opcion: ")

    cafes= {
        "1":"Cappuccino",
        "2": "Americano",
        "3": "TE",
        "4": "Expreso"
    }