# DEFINO FUNCIONES

def x_multiplos_de_y(numero,multiplo):
    multiplos=0
    for i in range(1,numero+1):
        multiplos = i*multiplo
        print(multiplo, "x",i,"=", multiplos)
    

def acum_ventas(ventas):
    cont=0
    acum=0
    for i in range(1,ventas+1):
        print("Importe para venta",i)
        importe=int(input("son pesos $ "))
        if importe>100:
            cont += 1 
            acum += importe
    print(" --- Las",cont,"ventas mayores a 100 pesos suman: $",acum,"---")
