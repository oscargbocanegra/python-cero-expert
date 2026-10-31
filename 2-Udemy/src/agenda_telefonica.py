from typing import Dict, Optional

agenda_telefonica: Dict[str, str] = dict()


def imprimir_operacion(nombre_operacion: str) -> None:
    print ("\n---------- Agenda Telefonica ----------")
    print (nombre_operacion)
    print ("---------------------------------------\n")

def agregar_contacto() -> None:
    print()
    nombre: str = input("Nombre del contacto: ").capitalize()
    numero: str = input("Numero del contacto: ")
    agenda_telefonica[nombre] = numero
    imprimir_operacion("* Contacto Agregado")

def remover_contacto() -> None:
    nombre: str = input("Nombre del contacto a remover: ").capitalize()
    nombre_operacion: Optional[str] = None

    try:
        del agenda_telefonica[nombre]
    except KeyError:
        nombre_operacion = "* Este contaacto no existe"
    else:
        nombre_operacion = "* Contacto Removido"
    imprimir_operacion(nombre_operacion)


def actualizar_contacto() -> None:
    nombre_operacion: Optional[str] = None
    nombre: str = input("Nombre del contacto a actualizar: ").capitalize()
    numero: str = input("Nuevo Numero del contacto: ")
    agenda_telefonica[nombre] = numero
    imprimir_operacion("* Contacto Actualizado")

def ver_contacto() -> None:
    nombre: str = input("Nombre del contacto: ").capitalize()
    nombre_operacion: Optional[str] = None
    
    try:
        nombre_operacion = "{} - {}".format(nombre, agenda_telefonica[nombre])
    except KeyError:
        nombre_operacion = "* Ese contacto No Existe"
    imprimir_operacion(nombre_operacion)


def ver_list_contactos() -> None:
    nombre_operacion: Optional[str] = None

    if len(agenda_telefonica) == 0:
        nombre_operacion = "* No tienes ningun contacto"
    else:
        for contacto in agenda_telefonica:
            if nombre_operacion == None:
                nombre_operacion = "{} - {}".format(contacto, agenda_telefonica[contacto])
            else:
                nombre_operacion += "\n{} - {}".format(contacto, agenda_telefonica[contacto])
    imprimir_operacion(nombre_operacion)

def iniciar_agenda() -> None:
    print ("Bienvenido a mi Agenda Telefonica...")
    while True:
        print()
        print ("1 - Agregar un contacto")
        print ("2 - Remover un contacto")
        print ("3 - Actalizar contactos")
        print ("4 - Ver un contacto")
        print ("5 - Ver todos los contactos")
        print ("6 - Salir")
        print()

        try:
            operacion: int = int(input("Escoja Opcion : "))
        except ValueError:
            imprimir_operacion("* Selecciona un numero de 1 a 6")
        else:
            if operacion == 1:
                agregar_contacto()
            elif operacion == 2:
                remover_contacto()
            elif operacion == 3:
                actualizar_contacto()
            elif operacion == 4:
                ver_contacto()
            elif operacion == 5:
                ver_list_contactos()
            elif operacion == 6:
                break
            else:
                imprimir_operacion("* Operacion Desconocida")

def dar_despedida() -> None:
    imprimir_operacion("* Gracias por usar nuestro servicio \nde Agendas Telefonicas")


iniciar_agenda()
dar_despedida()

