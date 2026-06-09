print("===Calculadora===")
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
while True:
    print("Menu de opciones")
    print("1. sumar ")
    print("2. restar ")
    print("3. multiplicar ")
    print("4. dividir ")

    opc = int(input("Ingrese una opcion "))
    if opc == 1:
        suma = numero1 + numero2
        print(f"La suma es: {suma}")
        break
    elif opc == 2:
        resta = numero1 - numero2
        print(f"La resta es: {resta}")
        break
    elif opc == 3:
        multi = numero1 * numero2
        print(f"La multiplicacion es : {multi}")
        break
    elif opc == 4:
        dividir = numero1/numero2
        print(f"La division es : {dividir}")
        break
