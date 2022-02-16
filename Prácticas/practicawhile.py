#############################################
#Elaborado por: Jose Fabio Navarro Naranjo. # 
#Fecha de creación:6/3/2019,9:11am          #
#última modificación:6/3/2019,9:17am        #
#Versión de Python:3.6.1                    #
#############################################

nombre=input("¿Cuál es su nombre?")
apellido=input(nombre+": ¿Cuál es su apellido?")
edad=int(input(nombre+" "+apellido+": ¿Cuál es su edad?"))
print(nombre+" "+apellido+", usted tiene"+" "+str(edad)+" "+"años.")
i=1
while i<=edad:
      print("Usted tiene: "+str(i)+" años")
      i+=1
if edad<13:
      print("Usted es un niño.")
elif edad<21:
      print("Usted es un adolescente.")
else:
      print("Usted es un adulto.")
