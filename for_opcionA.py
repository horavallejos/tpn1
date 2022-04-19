from for_funciones import *

#--------------------------------------------------------
# DEFINO LAS OPCIONES CON SUS RESPECTIVOS DATOS 
# PARA INGRESAR AL PROCEDIMIENTO

def opcionA():
    
    numero=int(input("Ingrese la cantidad de múltiplos buscados: "))
    multiplo=float(input("¿Múltiplos de qué numero querés?: "))
    
    x_multiplos_de_y(numero,multiplo) #funcion con parámetros
    
    print("")