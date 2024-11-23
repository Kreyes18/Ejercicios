import os
# Obtener la elección del primer jugador
eleccion_jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
while eleccion_jugador1 not in ["piedra", "papel", "tijera"]:
    print("Elección no válida. Inténtalo de nuevo.")
    eleccion_jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()

# Limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')

# Obtener la elección del segundo jugador
eleccion_jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()
while eleccion_jugador2 not in ["piedra", "papel", "tijera"]:
    print("Elección no válida. Inténtalo de nuevo.")
    eleccion_jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# Determinar el ganador
if eleccion_jugador1 == eleccion_jugador2:
    resultado = "Empate"
elif (eleccion_jugador1 == "piedra" and eleccion_jugador2 == "tijera") or \
     (eleccion_jugador1 == "papel" and eleccion_jugador2 == "piedra") or \
     (eleccion_jugador1 == "tijera" and eleccion_jugador2 == "papel"):
    resultado = "Jugador 1 gana"
else:
    resultado = "Jugador 2 gana"

# Mostrar el resultado
print(f"\nJugador 1 eligió: {eleccion_jugador1}")
print(f"Jugador 2 eligió: {eleccion_jugador2}")
print(f"Resultado: {resultado}")
