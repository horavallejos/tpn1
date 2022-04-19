from for_opcionA import opcionA
from for_opcionB import opcionB


def menu():
    print("")
    print("----------------------------------")
    print("A - CALCULAR MULTIPLOS")
    print("B - REGISTRAR VENTAS MAYORES A 100")
    print("X - Para salir del sistema")
    print("----------------------------------")

def inicio():
    menu()
    opcion=input(" --> Ingrese la opción que desea usar: ")
    print("")
    opciones(opcion)

#--------------------------------------------------------
# ESTE ES EL MENU DE OPCIONES Y EL CONDICIONAL

def opciones(opcion):
    if opcion == "A" or opcion == "a":
        # CALCULAR X CANTIDAD DE MULTIPLOS DE Y
        opcionA()
        inicio()
    
    elif opcion == "B" or opcion == "b":
        # LLAMO desde modulos.py al procedimiento acum_ventas
        opcionB()
        inicio()
        
    elif opcion == "X" or opcion == "x":
        salir=input("- N para seguir - S para salir - : ")
        if salir == "N" or salir == "n":
            inicio()
        else:
            print("")
            print(" - Gracias por usar nuestro sistema. Hasta pronto! - ")
            print("")