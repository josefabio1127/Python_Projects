###########################################
#Elaborado por: Jose Fabio Navarro Naranjo#
#Fecha de creación: 27/3/19, 8:14am       #
#Última modificación:                     #
#Versión: 3.6.1                           #
###########################################


#Definición de Funciones

def mostrarValList(plista):
    for n in plista:
        print(n)


def determinarMayorL(plista):
    mayor=0
    for n in plista:
        if n>mayor:
            mayor=n
    print(mayor)

def mostrarPares(plista):
    for n in plista:
        if n%2==0:
            print(n)

def encontrarCero(plista):
    if 0 in plista:
        print(True)
    else:
        print(False)
    return""    

def multiplicarImpar(plista):
    total=1
    for n in plista:
        if n%2!=0:
            total*=n
    return print(total)

def contarRepeticiones(plista,pnum):
    total=0
    for n in plista:
        if n==num:
            total+=1
    return print(total)
    
    
#Programa Principal
print("Mostrar Valores")
lista1=[5,8,3,4,9,1,2]
mostrarValList(lista1)
print("\nMayor de la lista")
lista2=[5,7,8,9,22,1,2,3,4,5,6,15]
determinarMayorL(lista2)
print("\nMostrar Pares")
lista3=[5,15,78,46,95,21,3,2,7,6]
mostrarPares(lista3)
print("\nEncontrar Cero")
lista4=[1,5,7,15,3,0,45,1,2,8]
print(encontrarCero(lista4))
print("\nMultiplicación Impares")
lista5=[1,5,4,6,7,8,9,2,3,15]
multiplicarImpar(lista5)
print("\nContar Repeticiones")
num=6
lista6=[1,9,5,45,6,8,2,1,6,7,9,15,4,6,62,9]
contarRepeticiones(lista6,num)

