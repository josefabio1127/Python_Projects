#############################################
#Elaborado por: Jose Fabio Navarro Naranjo. # 
#Fecha de creación:6/3/2019,7:30am          #
#última modificación:6/3/2019,9:01am        #
#Versión de Python:3.6.1                    #
#############################################

nombre=input("¿Cuál es su nombre?")
apellido=input(nombre+": ¿Cuál es su apellido?")
edad=int(input(nombre+" "+apellido+": ¿Cuál es su edad?"))
print(nombre+" "+apellido+", usted tiene"+" "+str(edad)+" "+"años.")
if edad>=18:
      print("Usted es mayor de edad.")
else:
      print("Usted es menor de edad.")
