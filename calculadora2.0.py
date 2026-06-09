print("===Calculadora===")

while True:
    print("Menu de opciones")
    print("1. sumar ")
    print("2. restar ")
    print("3. multiplicar ")
    print("4. dividir ")
    print("5. Salir ")
    opc = int(input("Ingrese una opcion "))
    
    if opc == 5:
        print("Saliendo")
        break
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    numero3 = int(input("Ingrese otro nummero: "))
    
    if opc == 1:
        suma = numero1 + numero2 + numero3
        print(f"La suma es: {suma}")
        
    elif opc == 2:
        resta = numero1 - numero2 - numero3
        print(f"La resta es: {resta}")
        
    elif opc == 3:
        multi = numero1 * numero2 * numero3
        print(f"La multiplicacion es : {multi}")
        
    elif opc == 4:
        dividir = numero1/numero2/numero3
        print(f"La division es : {dividir}")
        
    
