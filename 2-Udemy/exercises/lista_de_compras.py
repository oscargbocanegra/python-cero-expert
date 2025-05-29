# Agregar articulos.
# Remover articulos.
# Ver Articulos.
lista_articulos = list()

def agregar_articulo():
    print()
    articulo = input("Nombre del articulo a agregar: ")
    lista_articulos.append(articulo.capitalize())
    print("Articulo Agregado")
    print()


def remover_articulo():
    articulo = input("Nombre del articulo a Remover: ")
    lista_articulos.remove(articulo.capitalize())
    print("Articulo Removido")
    

def ver_articulos():
    print()
    print("--------- Lista de Compras ------------")
    for articulo in lista_articulos:
        print(articulo)
    print("---------------------------------------")

print ("Bienvenido a la lista de compras.. ")

while True:
    print()
    print ("Estas son las operaciones a realizar.. ")
    print ("1. Agregar articulos.. ")
    print ("2. Remover articulos.. ")
    print ("3. Ver los articulos.. ")
    print ("4. Salir.. ")
    print()
    operacion = int(input("Escoja Opcion : "))
    print()

    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulos()
    else:
        break
        print ("Gracias por usar nuestra lista de compras")