######################################################################
#Elaborado por: Emmanuel Naranjo Blanco y Jose Fabio Navarro Naranjo #
#Fecha de Creación: 18/03/2019 7:43pm                                #
#Fecha de última Modificación: 19/03/2019 10:00pm                    #
#Versión: 3.7.2                                                      #
######################################################################

#importación de librerías
import sys
sys.setrecursionlimit(5000)
"""
USO?
"""

#Definición de funciones
def determinarSumaAux(pnum): #1
    #Funcionamiento: Validar los datos para calcular la sumatoria dado un numero entero positivo.
    #Entradas: numero(int)
    #Salidas: sumatoria(float)
    if isinstance(pnum,int) and pnum>0:
        return determinarSuma(pnum)
    else:
        return 'El digito insertado debe ser tipo entero y positivo'

def determinarSuma(pnum):
    """
    Funcionamiento: Calcular la sumatoria dado un numero entero positivo
    Entradas: numero(int)
    Salidas: sumatoria(float)
    """
    suma=0
    i=1
    while i<=pnum:
       suma+=((-1)**i)*1/(i**2)
       i+=1
    return 'El resultado es '+str(suma)
#-------------------------------------------------------------------------------

def contarDigitosAux(pnum):#2
    #Funcionamiento: Validar los datos para contar los dígitos de un número. 
    #Entradas: numero(int)
    #Salidas: cantidad de Digitos(int)
    if isinstance(pnum,int) and pnum>0:
        return contarDigitos(pnum)
    else:
        return "El digito insertado debe ser tipo entero y positivo."

def contarDigitos(pnum):
    """
    Funcion: Contar los dígitos de un número.
    Entrada: numero(int)
    Salida: cantidad de Digitos(int)
    """
    cantDigitos=0
    while pnum!=0:
        pnum=pnum//10
        cantDigitos+=1
    else:
        return "El número tiene "+str(cantDigitos)+" digitos."
#-------------------------------------------------------------------------------

def sumarEnterosAux(pnum):#3
    #Funcionamiento: Validar los datos para sumar los dígitos de un número. 
    #Entradas: numero(int)
    #Salidas: resultado de la suma de enteros(int)
    if isinstance(pnum,int) and pnum>0:
        return sumarEnteros(pnum)
    else:
        return 'El digito insertado debe ser tipo entero y positivo'
    
def sumarEnteros(pnum):
    """
    Funcion: Sumar los dígitos de un número.
    Entrada: numero(int)
    Salida: resultado de la suma de enteros(int)
    """
    suma=0
    while pnum!=0:
        suma+=pnum%10
        pnum=pnum//10
    else:
        return "La suma de los de dígitos es :"+str(suma)
#-------------------------------------------------------------------------------

def mostrarParesAux(pnum):#4
    #Funcionamiento: Validar los datos para mostrar los dígitos pares de un número. 
    #Entradas: numero(int)
    #Salidas: digitos pares(int)
    if isinstance(pnum,int) and pnum>0:
        return mostrarPares(pnum)
    else:
        return 'El digito insertado debe ser tipo entero y positivo.'

def mostrarPares(pnum):
    """
    Funcion: Mostrar los digitos que son pares en la expresión.
    Entrada: numero(int)
    Salida: digitos pares(int)
    """
    print('Los elementos pares del numero son: ')#######
    while pnum!=0:
        n=pnum%10
        if n%2==0:
            print(n)
        pnum=pnum//10
    return ''

#-------------------------------------------------------------------------------

def obtenerCantidadesAux(pnum):#5
    #Funcionamiento: Validar los datos para mostrar la cantidad de dígitos pares e impares de un número. 
    #Entradas: numero(int)
    #Salidas: cantidad de digitos pares e impares(int)
    if isinstance(pnum,int) and pnum>0:
        return obtenerCantidades(pnum)
    else:
        return 'El digito insertado debe ser tipo entero y positivo.'

def obtenerCantidades(pnum):
    """
    Funcion: Mostrar la cantidad de digitos pares e impares en la expresión.
    Entrada: numero(int)
    Salida: cantidad de digitos pares e impares(int)
    """
    par=0
    impar=0
    while pnum!=0:
        n=pnum%10
        if n%2==0:
            par+=1
        else:
            impar+=1
        pnum=pnum//10
    return "La expresión tiene "+str(par)+" dígitos pares y "+str(impar)+" digitos impares."
#-------------------------------------------------------------------------------

def contarRepeticionesAux(pnum,pcifra): #6
    #Funcionamiento:Validar los datos para buscar las repeticiones de una cifra
    #Entradas: numero(int),cifra a buscar(int)
    #Salidas: cantidad de veces que aparece la cifra(int)
    
    if isinstance (pnum,int) and pnum>0:
        if isinstance(pcifra,int) and pcifra>0 and pcifra<=9:
            return contarRepeticiones(pnum,pcifra)
        else:
            return 'La cifra a buscar en el numero debe ser positiva y menor a 10.'
    else:
        return 'El numero insertado debe ser entero y positivo.'


def contarRepeticiones(pnum,pcifra):
    """
    Funcion: Calcular la cantidad de veces que aparece un digito en un numero dado
    Entrada: numero(int),cifra a buscar(int)
    Salida: cantidad de veces que aparece la cifra(int)
    """
    contador=0
    while pnum!=0:
        if pnum%10==pcifra:
            pnum//=10
            contador+=1
        else:
            pnum//=10
    else:
        return "La cifra buscada aparece "+str(contador)+" veces."
    





