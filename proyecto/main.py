from  menu import mostrar_menu 
from pedidos import pedir_cafe

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
           pedir_cafe()
        elif opcion == "2":
            pass
        elif opcion == "3":
            print("Muchas gracias por usar la cafeteria!!")
            break 
        else:
            print("Opcion incorrecta seleccione otra opcion ")



if __name__ == "__main__":
    main()   