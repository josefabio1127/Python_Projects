######################################################################
#Elaborado por: Emmanuel Naranjo Blanco y Jose Fabio Navarro Naranjo #
#Fecha de Creación: 18/03/2019 7:43pm                                #
#Fecha de última Modificación: 19/03/2019 10:00pm                    #
#Versión: 3.7.2                                                      #
######################################################################

#importanción de librerías
from funcionesit import*
""""funcionesit" es el archivo que contiene las funciones principales
a ser llamadas desde este archivo"""

#Definición de funciones
#Permiten el ingreso y salida de datos

def opcionSumaAcumulada():#1
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: La sumatoria segun la formula dada
    """ 

    print ("\n------------------------\n")
    print("Prueba de la sumatoria dado un numero\n")
    num=int(input('Coloque un numero: '))
    print(determinarSumaAux(num))
    
def opcionCantidadDigitos():#2
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: La cantidad de digitos del número
    """ 
    
    print ("\n------------------------\n")
    print("Cantidad de digitos de un número\n")
    num=int(input("Coloque un número entero: "))
    print(contarDigitosAux(num))
    
def opcionSumaEnteros():#3
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: La suma de los dígitos del número 
    """ 
    
    print ("\n------------------------\n")
    print("Suma de Dígitos\n")
    num=int(input("Coloque un número entero: "))
    print(sumarEnterosAux(num))
    
def opcionMostrarPares():#4
    """ 
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: números pares de la expresión
    """ #ojo
    
    print ("\n------------------------\n")
    print("Mostrar Pares\n")
    num=int(input("Coloque un número entero: "))
    print(mostrarParesAux(num))
    
def opcionCantidadParImpar():#5
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: cantidad de dígitos pares e impares de la expresión. 
    """ #ojo
    
    print ("\n------------------------\n")
    print("Cantidad de pares e impares\n")
    num=int(input("Coloque un número entero: "))
    print(obtenerCantidadesAux(num))
    
def opcionRepeticiones():#6
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: cantidad de veces que aparece un numero dado
    """ #ojo
    print ("\n------------------------\n")
    print("Repeticiones de una cifra en un numero\n")
    num=int(input('Coloque un numero entero: '))
    cifra=int(input('Coloque la cifra a saber sus repeticiones: '))
    print(contarRepeticionesAux(num,cifra))

###############################################################################

def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    print("\n**************************\n")
    print("Trabajo con iteración")
    print("\n**************************\n")
    print("1. Sumatoria")
    print("2. Cantidad de digitos de un numero")
    print("3. Suma de digitos de un numero entero")
    print("4. Mostrar numeros pares de una cifra numerica")
    print("5. Cantidad de pares e impares en un numero")
    print("6. Cantidad de apariciones de un numero")
    print("0. Terminar")
    opcion = int (input ("Escoja una opción: "))
    if opcion >=0 and opcion <=6:   
        if opcion==1:
            opcionSumaAcumulada()
        elif opcion==2 :
            opcionCantidadDigitos()
        elif opcion==3:
            opcionSumaEnteros()
        elif opcion==4:
            opcionMostrarPares()
        elif opcion==5:
            opcionCantidadParImpar()
        elif opcion==6:   
            opcionRepeticiones()
        elif opcion==0:
            return
    else:
        print ("Opción inválida")

    menu()

#inicio del Programa Principal
menu()


    
