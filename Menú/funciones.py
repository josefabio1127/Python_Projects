######################################################################
#Elaborado por: Emmanuel Naranjo Blanco y Jose Fabio Navarro Naranjo #
#Fecha de Creación: 18/03/2019 5:00pm                                #
#Fecha de última Modificación: 19/03/2019 1:16am                     #
#Versión: 3.7.2                                                      #
######################################################################

#importación de librerías
import sys
sys.setrecursionlimit(5000)

#Definición de funciones   
def esBisiesto(a):#1
    """
    Funcion: Analiza si un año es bisiesto o no. 
    Entrada: a(int)Recibe un número entero mayor que cero que representa un año
    Salida: Devuelve True/False si corresponde a un año bisiesto o no
    """
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def masCercanos(n1, n2, n3, n4):#2
    """
    Funcion: Determina el número más cercano a cero sin importar si es positivo o negativo. 
    Entrada: Recibe 4 números enteros del usuario.
    Restricciones : Los cuatros números pueden ser negativos, cero, positivos
    Salida: Devuelve una hilera o texto con el número más ceracano. 
    """
    dn1 = abs(n1)
    dn2 = abs(n2)
    dn3 = abs(n3)
    dn4 = abs(n4)

    distanciaMenor = min(dn1,dn2,dn3,dn4)

    hilera = "Números más cercanos al cero: \n"      # \ : alt+92
    if distanciaMenor == dn1:
        hilera += str(n1)

    if distanciaMenor == dn2:
        hilera += " " + str(n2)

    if distanciaMenor == dn3:
        hilera += " " + str(n3)

    if distanciaMenor == dn4:
        hilera += " " + str(n4)

    return hilera

def calcularTarifa(pactual,pporc):#3
        """
        Funcionamiento:Calcular el aumento de la tarifa de buses
        Entradas:montoActual(int), porcentaje(int)
        Salidas: monto aumentado (float)
        """
        aumento=(pactual*pporc)/100
        nuevo=pactual+aumento
        #return pactual+((pactual*pporc)/100)
        return nuevo
    
def calcularTarifaAux(pactual,pporc): #3
        #Funcionamiento:Validar las entradas para el calculo de aumento
        #Entradas:actual(int), porcentaje(int)
        #Salidas: monto aumentado (float)
        if isinstance(pactual,int) and isinstance(pporc,int):
                if pactual>0 and pporc>0:
                        return calcularTarifa(pactual,pporc)
                else:
                        return "Los valores "+str(pactual)+","+str(pporc)+ ": deben ser mayores a 0."
        else:
               return "Los datos de ingreso deben ser de tipo entero"
def calcularImcAux(ppeso,paltura):
    """
        Funcionamiento:Validar la entradas para el cálculo del IMC
        Entradas:peso(int), estatura(float)
        Salidas: monto aumentado (float)
    """
    if isinstance(ppeso,float) and isinstance(paltura,float):
        if ppeso>0 and paltura>0:
            return calcularImc(ppeso,paltura)
        else: 
            return "Los valores "+str(ppeso)+","+str(paltura)+ ": deben ser mayores a 0."
    else:
        return "Los datos de ingreso deben ser de tipo entero."

def calcularImc(ppeso,paltura):#4
    """
        Funcionamiento:Calcular el índice de masa corporal.
        Entradas:ppeso(int), pestatura(float)
        Salidas: índice de masa corporal(str)
    """
    imc=ppeso/(paltura)**2
    if imc<=18.5:
        return "bajo peso"
    elif imc<=25:
        return"Peso normal"
    elif imc<=30:
        return"Sobrepeso"
    elif imc<=35:
        return "Obesidad 1"
    elif imc<=40:
        return"Obesidad 2"
    elif imc<=50:
        return"Obesidad 3"
    elif imc>50:
        return"Obesidad 4"

def calcularTablaMulti(pnum):#5
    """
        Funcionamiento: Imprimir la tabla de multiplicar del número dado
        Entradas:pnum
        Salidas:Tabla de multiplicar del número dado
    """
    print("Tabla del ",str(pnum))
    i=1
    while i<=10:
        resultado=print(pnum," x ",i," = ",pnum*i)
        i+=1
    return " "
        
        

def aplicarRangoAux(pnumero1,pnumero2): #6
    #Funcionamiento: Validar las entradas para saber el rango de tablas de multiplicar si el primer digito es menor al segundo
    #Entradas: pnumero1(int),pnumero2(int)
    #Salidas: nombre de la tabla(str) y rango de tablas de multiplicar(int)
    if isinstance(pnumero1,int) and isinstance(pnumero2,int):
        if pnumero1<=pnumero2:
            return aplicarRango(pnumero1,pnumero2)
        else:
            return 'El primer digito debe ser menor al segundo.'
    
    
def aplicarRango(pnumero1,pnumero2):
    """
    Funcionamiento: Calcular el rango de tablas de multiplicar si el primer digito es menor al segundo
    Entradas: pnumero1(int),pnumero2(int)
    Salidas: nombre de la tabla(str) y rango de las tablas de multiplicar(int) 
    """
    i=pnumero1
    while i<=pnumero2:
        j=0
        print("\n","tabla del ",i,"\n")
        while j<=10:
            print(str(i),"*",str(j),"=",str(i*j))
            j+=1
        else:
            i+=1
    else:        
        return '\n' #none?

    
def determinarSumaAux(pnumero): #7
    #Funcionamiento: Validar las entradas para saber la sumatoria dado un numero entero positivo
    #Entradas: pnumero(int)
    #Salidas: sumatoria(float)
    if isinstance(pnumero,int):
        if pnumero>0:
            return determinarSuma(pnumero)
        else:
            return 'El digito insertado debe ser positivo'
    
    
def determinarSuma(pnumero):
    """
    Funcionamiento: Calcular la sumatoria dado un numero entero positivo
    Entradas: pnumero(int)
    Salidas: sumatoria(float)
    """
    suma=0
    i=1
    while i<=pnumero:
       suma+=(-1)**i*1/(i**2)
       i+=1
    return 'El resultado es '+str(suma)

            
def saberTrianguloAux(pangulo1,pangulo2,pangulo3):#8
    #Funcionamiento:Validar las entradas para saber el tipo de triangulo
    #Entradas:pangulo1(float), pangulo2(float), pangulo3(float)
    #Salidas: tipo de triangulo(str)
    if isinstance(pangulo1,float) and isinstance(pangulo2,float) and isinstance(pangulo1,float):
        if pangulo1+pangulo2+pangulo3==180 and pangulo1>0 and pangulo2>0 and pangulo3>0:
            return saberTriangulo(pangulo1,pangulo2,pangulo3)
        else:
            return 'Los 3 angulos del triangulo '+str(pangulo1)+', '+str(pangulo2)+', '+str(pangulo3)+' y deben sumar 180 grados y ser positivos.'        

def saberTriangulo(pangulo1,pangulo2,pangulo3):
    """
    #Funcionamiento:Validar las entradas para saber el tipo de triangulo
    #Entradas:pangulo1(float), pangulo2(float), pangulo3(float)
    #Salidas: tipo de triangulo(str)
    """
    if pangulo1<90 and pangulo2<90 and pangulo3<90:
        return 'Su triangulo es acutangulo.'
    elif pangulo1==90 or pangulo2==90 or pangulo3==90:
        return 'Su triangulo es rectangulo.'
    elif pangulo1>90 or pangulo2>90 or pangulo>90:
        return 'Su triangulo es obtusangulo.'
    
def calcularMultiCorrect(pfact1,pfact2,presult):
    """
    #Funcionamiento:Validar las entradas para saber el tipo de triangulo
    #Entradas:pangulo1(float), pangulo2(float), pangulo3(float)
    #Salidas: tipo de triangulo(str)
    """
    if pfact1*pfact2==presult:
        return "Resultado correcto"
    else:
        print("Resultado incorrecto, el resultado correcto es: ",pfact1*pfact2)
        return" "

def calcularEstadoAlum(pnota):
    """
    #Funcionamiento:Validar las entradas para saber el tipo de triangulo
    #Entradas:pangulo1(float), pangulo2(float), pangulo3(float)
    #Salidas: tipo de triangulo(str)
    """
    if pnota>=67.5:
        return "Está aprobado"
    elif pnota>=57.5:
        return "Puede ir a reposición"
    elif pnota<57.5:
        return "Está reprobado"
    
##############################################################################
def potencia(a,b):
    """
    Funcion:  
    Entradas: 
    Salidas: 
    """
    if a==0 and b==0:
        return "Error"
    elif a==0:
        return a
    elif b==0:
        return 1
    elif b <0:
        return 1 / potencia(a, -b)
    else:
        return a * potencia (a, b-1)

def esPrimoAux(n, divisor):
    """
    Funcion:  
    Entradas: 
    Salidas: 
    """
    if divisor < n//2:
        if n%divisor ==0:
            return False
        else:
            return esPrimoAux(n, divisor+2)
    else:
        return True

def esPrimo(n):
    """
    Funcion:  
    Entradas: 
    Salidas: 
    """
    if n==2:
        return True
    elif n%2==0:
        return False
    else:
        divisor=3
        return esPrimoAux(n, divisor)


def primosEntre(desde, hasta):
    """
    Función: Encuentra todos los primos encontrados en un rango.  
    Entrada: Se reciben dos valores enteros que representan un rango.
    Salida: Devolver los números primos contenidos en ese rango
    Restriccion : desde < hasta y desde >= 2
    """
    if desde ==  2:
        return str(desde) + " " + primosEntre(desde+1, hasta)
    elif desde %2==0:
        return primosEntre(desde+1, hasta)
    else:
        if desde <= hasta:
            if esPrimo(desde) == True:
                return str(desde) + " " + primosEntre(desde+2, hasta)
            else:
                return primosEntre(desde+2, hasta)
        else:
            return ""
##############################################################################
