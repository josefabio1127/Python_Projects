def calcTablas(f1,f2):
    n=1
    while n<=10:
        x=print(f1,"x",n,"=",f1*n)
        n+=1
    return x

n1=int(input("Inserte un número"))
n2=int(input("Inserte un número mayor al primero"))
while n1<=n2:
    print("Tabla del ",n1)
    print(calcTablas(n1,n2))
    n1+=1

