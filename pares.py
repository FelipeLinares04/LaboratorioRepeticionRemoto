print("cuando un numero es par?")
x=int(input("Ingrese el termino "))
contador1=0
contador2=0
for i in range(1,x+1):
    a=int(input("da el numero que quieras "))
    if a==0:
        print("su numero es cero, se detiene el algoritmo")
        break


    if a%2==0:
        print("su numero es par")
        contador1=contador1+1

    else:
        print("su numero es impar")
        contador2=contador2+1


print(f"hay {contador1} numeros pares")
print(f"hay {contador2} numeros impares")



