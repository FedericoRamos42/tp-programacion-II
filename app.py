from mazo import Mazo
from jugador import Jugador
from datos import *

def login() -> Jugador:
    nombre_de_usuario = input("Ingrese su nombre: ")
    contrasena = input("Ingrese su contraseña: ")
    
    for usuario in jugadores:
        if usuario.nombre == nombre_de_usuario and usuario.contrasena == contrasena:
            print(f"Bienvenido {nombre_de_usuario}")
            return usuario
        else:
            print(f"Usuario {nombre_de_usuario} no encontrado")
            return None #hace que el while sea falso.
    
    
def menu() -> None:
    print("1. Iniciar Sesion")
    print("2. Salir")
    
def mostrar_menu():
    print("1. Crear mazo")
    print("2. Editar mazo")
    print("3. Iniciar Partida")
    print("4. Cerrar Sesion")

def menu_mazo():
    print("1. Agregar carta")
    print("2. Eliminar carta")
    print("3. Subir nivel")
    print("4. Salir")

while True:
    menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        usuario = login()
        while usuario:
            mostrar_menu()
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                print(f"{usuario.nombre}, selecciona tus cartas para el mazo.")
                while len(usuario.mazo.cartas) < 8: #mostrar mensaje cuando el mazo esta completo
                    print("Cartas disponibles:")
                    for i, carta in enumerate(cartas, 1):
                        print(f"{i}. {carta}")
                    seleccion = int(input("Seleccione el número de la carta que desea agregar: ")) - 1
                    if 0 <= seleccion < len(cartas):
                        carta_elegida = cartas[seleccion]

                        if usuario.elegir_mazo(carta_elegida):
                           print(f"{usuario.nombre} ha agregado {carta_elegida.nombre} al mazo.")
                        else:
                            print(f"{usuario.nombre} ya tiene {carta_elegida.nombre} en su mazo.")
                    else:
                        print("Selección no válida. Intente de nuevo.")
            elif opcion == 2:
                menu_mazo()
                opcion = int(input("Seleccione una opción: "))
                for i, carta in enumerate(usuario.mazo.cartas, 1):
                    print(f"{i}. {carta}")
                if opcion == 1:
                    pass
            elif opcion == 3:
               usuario.iniciar_partida()
            elif opcion == 4:
               print("Saliendo...")
               break
    elif opcion == 2:
        print("Saliendo...")
        break

    
# def mostrar_menu():
#     print("1. Crear Jugador")
#     print("2. Ver Jugadores")
#     print("3. Iniciar Partida")
#     print("4. Salir")


# jugador = Jugador('joaquin', 2, 4)
# jugador.elegir_mazo()

# print('-----------------------------')
# for i, carta in enumerate(jugador.mazo.cartas, 1):
#     print(f"{i}. {carta}")
# print('modificar mazo:')
# carta =  int(input('que carta quiere quitar:'))   - 1
# carta_seleccionada = jugador.mazo.cartas[carta] 
# jugador.mazo.remove_carta(carta_seleccionada)
# print('-----------------------------')
# print(jugador.mazo)