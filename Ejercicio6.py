a = float(input("Inserte un numero "))
print()
b = float(input("Inserte otro numero "))
print()

diccionario = {1: lambda a,b: a + b, 2: lambda a,b: a-b, 3: lambda a,b: a*b, 4: lambda a,b: a/b}

tema = int(input('Elige un tema: \n 1: suma \n 2: resta \n 3: multiplicacion \n 4: division'))
print()

print ("El resultado es: " , float(diccionario[tema](a,b)))

x = input() #Se utilizó esta variable para apretar Enter, indicando que finalizo el programa (fuera de Geany), ya que sino se cierra, impidiendo que se muestre el resultado en pantalla 



