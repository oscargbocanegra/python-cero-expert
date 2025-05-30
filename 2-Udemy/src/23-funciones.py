edad = 21



## Llamando a una función.
def solicitud_ingreso(edad):
    if edad < 10:
        print ('No Puedes Ingresar')
    elif edad >= 21:
        print ('Si puedes ingresar'.upper())
    else:
        print('Ya tienes edad para ingresar')

solicitud_ingreso(25)