print("Cuando un numero es primo")
x=int(input("Ingresar numeros enteros"))
a=2
m=True
while a<x:
    if x%a==0:
        print("El numero no es primo")
        m=False
        break
    a=a+1

if m==True:
    print("El numero es primo")




