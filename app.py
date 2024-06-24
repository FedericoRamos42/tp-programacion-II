from mazo import Mazo
from jugador import Jugador
from datos import *

def mostrar_menu():
    print("1. Crear Jugador")
    print("2. Ver Jugadores")
    print("3. Iniciar Partida")
    print("4. Salir")


jugador = Jugador('joaquin', 2, 4)
jugador.elegir_mazo()

print('-----------------------------')
print(jugador.mazo)
print('modificar mazo:')
carta =  int(input('que carta quiere quitar:'))   - 1
carta_seleccionada = jugador.mazo.cartas[carta] 
jugador.mazo.remove_carta(carta_seleccionada)
print('-----------------------------')
print(jugador.mazo)