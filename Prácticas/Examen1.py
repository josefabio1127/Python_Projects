#Creado por: Jose Fabio Navarro Naranjo.
#Carnet: 2019049626
#Fecha: 17/05/2019
#Versión: 3.7.2

#Examen 2, Elementos de Computación

#Parte 1 String

def analizarTexto(texto):
    """
    Funcionamiento: devolver un URL por partes específicas.
    Entradas: texto.
    Salidas: partes de un URL y el nombre del dominio letra por letra.
    """
    print("Protocolo de Carga: "+texto[:4])
    print("Formato de Página: "+texto[7:10])
    print("Nombre del Dominio del Sitio: "+texto[11:])
    x=11
    while x<len(texto):
        print(texto[x])
        x+=1
    return

#Parte 2 Matrices y Listas

def analizarMatrizAux(notas):
    """
    Funcionamiento: Validar el ingreso de la matriz de notas.
    Entradas: matriz de notas.
    Salidas: matriz validada.
    """
    for x in notas:
        if x==[]: #aquí me faltó poner un = y poner los :
            print("La matriz está vacía.")
            return
        elif len(x)!=8:
            print("La matriz debe tener 8 columnas.")
            return
    return analizarMatriz(notas)
    
def analizarMatriz(notas):
    """
    Funcionamiento: identificar la nota mayor y menor, determinar el promedio y la condición del estudiante.
    Entradas: matriz de notas
    Salidas: lista con nota mayor y menor, promedio y condición.
    """
    for x in notas: #faltaban los :
        suma=0
        mayor=0
        menor=100
        for nota in x:
            if mayor<nota:
                mayor=nota
            if menor>nota:
                menor=nota
            suma+=nota
        prom=suma/8
        condicion=""
        if prom>70:
            condicion="Aprobado"
        else:
            condicion="Reprobado"
        lista=[mayor,menor,prom,condicion]#coloqué esta línea en el print
        print(lista)
    return

#Parte 3 Diccionarios

#Funcion A
def registrarAlumnos(diccionario):
    """
    Funcionamiento: añadir los datos de un estudiante a un diccionario.
    Entradas: diccionario vacío.
    Salidas: diccionario lleno.
    """
    nombre=input("Ingrese el nombre: ")
    carnet=input("Ingrese el número de carnet: ")
    sexo=input("Ingrese el sexo(1 si es hombre, 2 si es mujer): ")
    if sexo=="1": #faltaban las "" del 1
        sexo=True
    else:
        sexo=False
    diccionario[carnet]=[nombre,sexo]
    return diccionario

#Funcion B
def mostrarClase(diccionario):
    """
    Funcionamiento:Devuelve los datos del estudiante.
    Entradas: diccionario lleno.
    Salidas: cada dato del diccionario por separado.
    """
    llaves=list(diccionario.keys())
    x=0
    while x<len(llaves):
        print("Carnet: "+str(llaves[x]))
        print("Nombre: "+str(diccionario[llaves[x]][0]))
        if diccionario[llaves[x]][1]==True:
            print("Sexo: Masculino")
        elif diccionario[llaves[x]][1]==False:
            print("Sexo: Femenino")
        x+=1
    return

#Programas Principales

#Programa principal del ejercicio 1
texto="http://www.google.com"
analizarTexto(texto)

#Programa principal del ejercicio 2
matriz=[[87,95,11,22,65,78,98,27],[32,69,57,38,26,98,26,90]]
#matriz=[[]]
#matriz=[[1,2,3,4,5,6,7]]
analizarMatrizAux(matriz)

#Programa principal del ejercicio 3
diccionario={}
registrarAlumnos(diccionario)
mostrarClase(diccionario)
