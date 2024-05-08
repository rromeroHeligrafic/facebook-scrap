#Voy a crear una calculadora

#primer paso elejir la operacion
opcion = input("""
Ingrese el numero de su opcion:                
1 - suma
2 - resta
3 - multiplicaciona
4 - division
5 - salir
""")

#ingresar el primer numero por consola
numero1 = int(input("escriba el primer numero: "))
#ingresar el segundo numero por consola
numero2 = int(input("escriba el segundo numero: "))

#imprimir el mensaje
if opcion == "1":
    print(numero1 + numero2)
if opcion == "2":
    print(numero1 - numero2)
if opcion == "3":
    print(numero1 * numero2)
if opcion == "4":
    print(numero1 / numero2)
if opcion == "5":
    print("adios")
else:
    print("no es una operacion")
