#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 11/4/2019  12:00pm 
#Fecha de última Modificación: 13/4/2019  12:16am
#Versión: 3.7.2

amigos=[]
meses=[["Enero",0],["Febrero",0],["Marzo",0],["Abril",0],["Mayo",0],["Junio",0],["Julio",0],["Agosto",0],["Setiembre",0],["Octubre",0],["Noviembre",0],["Diciembre",0]]
aux=[1,2]
hombres=[]
mujeres=[]



def ingresarAmigos():
    """
    Funcionamiento: Permite el ingreso de los amigos, sus fechas de cumpleaños y su sexo.
    Entradas: N/A
    Salidas: matriz "amigos" llena.
    """
    continuar=1
    while continuar==1:
        datos=[]
        #nombre
        datos.append(input("1. Ingrese el nombre de su amig@: "))#posicion 0
        datos[0]=datos[0].title()
        #sexo
        datos.append(int(input("2. Ingrese el sexo de su amig@ (hombre(1) o mujer (2)): ")))#posicion 1
        while datos[1] not in aux: #¿usted cree que esto sea mejor ponerlo en otra funcion, para respetar que cada funcion no haga mas de una accion?
            print("Dato inválido.")
            datos[1]=int(input("2. Ingrese el sexo de su amig@ (hombre(1) o mujer (2)): "))
        #sexoAux(datos)
        #mes
        datos.append(input("3. ¿En qué mes cumple "+datos[0]+"?(ej: enero)"))#posicion 2
        datos[2]=datos[2].capitalize()#.title()(creo que sería lo mismo capitalize que title porque el mes es solo una palabra) 
        contarMeses(datos)
        #dia
        datos.append(int(input("4. ¿Qué día cumple "+datos[0]+"?")))#posicion 3
        diaAux(datos)
        amigos.append(datos)
        print('\n----------------------------------\n')
        continuar=int(input("Si desea ingresar otro amigo presione 1, sino presione 2: "))
        print('\n----------------------------------\n')
    return

def diaAux(datos):
    """
    Funcionamiento: valida que el número de día ingresado sea correcto.
    Entradas: lista "datos"
    Salidas: lista "datos"
    """
    while datos[3]<1 or datos[3]>31:
        print("Número inválido.")
        datos[3]=int(input("4. Qué día cumple "+datos[0]+"?"))
    return

#porque no dejamos esta función para que valide el ingreso del numero del sexo??
'''
def SaberSexoAux(datos): 
    if datos[1]==1:
        hombres.append(1)
    elif datos[1]==2:
        mujeres.append(1)
    else:
        while datos[1] not in aux:
            print("Dato inválido.")
            datos[1]=input("Ingrese el sexo de su amig@ (hombre(1) o mujer (2)): ")
        return
'''
def contarMeses(datos):
    """
    Funcionamiento: cuenta cuantos amigos hay en cada mes y valida el ingreso de los meses
    Entradas: lista datos
    Salidas: datos[2]
    """
    if datos[2]==meses[0][0]:
        meses[0][1]+=1
    elif datos[2]==meses[1][0]:
        meses[1][1]+=1
    elif datos[2]==meses[2][0]:
        meses[2][1]+=1
    elif datos[2]==meses[3][0]:
        meses[3][1]+=1
    elif datos[2]==meses[4][0]:
        meses[4][1]+=1
    elif datos[2]==meses[5][0]:
        meses[5][1]+=1
    elif datos[2]==meses[6][0]:
        meses[6][1]+=1
    elif datos[2]==meses[7][0]:
        meses[7][1]+=1
    elif datos[2]==meses[8][0]:
        meses[8][1]+=1
    elif datos[2]==meses[9][0]:
        meses[9][1]+=1
    elif datos[2]==meses[10][0]:
        meses[10][1]+=1
    elif datos[2]==meses[11][0]:
        meses[11][1]+=1
    else:
        x=False
        while x==False:
            print("Nombre del mes inválido.")
            datos[2]=input("3. ¿En qué mes cumple "+datos[0]+"?")
            datos[2]=datos[2].capitalize()
            n=0
            while n<12:
                if datos[2]==meses[n][0]:
                    x=True
                n+=1
        contarMeses(datos)
    return
   

def imprimirResultado():
    """
    Funcionamiento: imprime la lista de amigos
    Entradas: N/A
    Salidas: lista de amigos
    """
    n=0
    while n<12:
        a=0
        if meses[n][1]>0:
            print("En "+meses[n][0]+" cumplen "+str(meses[n][1])+" amigos, ellos son:")
            while a<len(amigos):
                if amigos[a][2]==meses[n][0]:
                    print(amigos[a][0]+" el día "+str(amigos[a][3]))
                a+=1
        else:
            print("En "+meses[n][0]+" cumplen "+str(meses[n][1])+" amigos.")
            while a<len(amigos):
                if amigos[a][2]==meses[n][0]:
                    print(amigos[a][0]+" el día "+str(amigos[a][3]))
                a+=1
        n+=1
    return

def saberSexo(amigos):  #mae creo que esta funcion se puede dividir en 2,
                        #una que realice el conteo de hombres y mujeres y
                        #además valide que entren solo 1 y 2, y otra que
                        #imprima lo de los amigos hombres y mujeres, porque
                        #esta funcion está haciendo más de una accion. ademas
                        #falta documentar
    hombres=0
    mujeres=0
    j=0
    while j<len(amigos):
        if amigos[j][1]==1:
            hombres+=1
        else:
            mujeres+=1
        j+=1
    print('\n----------------------------------\n')
    print('Usted tiene ',hombres,' amigo(s) y ',mujeres,' amiga(s).')
    if hombres>mujeres:
        print('Por lo tanto, usted tiene mas amigos hombres que mujeres')
    elif hombres<mujeres:
        print('Por lo tanto, usted tiene mas amigas mujeres que hombres')
    elif hombres==mujeres:
        print('Usted tiene la misma cantidad de amigos como amigas')
    
    return ''

    
