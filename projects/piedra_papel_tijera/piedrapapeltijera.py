import random

# Opciones disponibles
opciones = ["piedra", "papel", "tijera"]

# Función para determinar el ganador
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

# Bucle principal del juego
while True:
    # Elección del usuario
    usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
    
    if usuario == "salir":
        break
    if usuario not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        continue
    
    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    
    # Determinar el ganador
    resultado = determinar_ganador(usuario, computadora)
    print(resultado)