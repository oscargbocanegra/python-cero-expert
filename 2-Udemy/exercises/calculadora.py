# Desplegar las instrucciones.
"""
1. Obtener el numero de operaciones. 2. Obtener los numeros del usuario.
3. Realizar la operacion en base a la peticion del usuario. 4. Desplegar el resultado.
5. Preguntar si quiere realizar otra operacion
"""
def operacion_calc(operacion,numero1,numero2):
    if operacion == 1:
        return numero1 + numero2
    elif operacion == 2:
        return numero1 - numero2
    elif operacion == 3:
        return numero1 * numero2
    elif operacion == 4:
        return numero1 / numero2


print ("Bienvenido a la calculadora en python")

while True:
    print ("Las siguientes operaciones estan programadas.")
    print ("1 - Suma.")
    print ("2 - Resta.")
    print ("3 - Multiplicacion.")
    print ("4 - Division.")

    try:
        operacion = int(input("Intruce la operacion a realizar: "))
        numero1 = int(input("Introduce el primer numero: "))
        numero2 = int(input("Introduce el segundo numero: "))
    except:
        print ("Introduce solo Numeros")
    else:
        if operacion < 1 or operacion > 4:
            print ("\n !!! Esta Operacion No es valida Intenta nuevamente !!!!!!!!!!!!")
            continue
        
        resultado  = operacion_calc(operacion,numero1,numero2)
        print ("El resultado es: " + str(resultado))
        continuar = input("Deseas continuar? si/no : ")
        print ()
        print ()
        
        if continuar != "si":
            break
print ("Gracias por usar la calculadora")