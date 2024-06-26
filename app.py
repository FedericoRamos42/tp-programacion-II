from jugador import Jugador
from datos import *
from carta import Carta
from partida import Partida

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
            mostrar_menu() # Sub menu para cuando el usuario ya esta logueado
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1: # Jugador arma su mazo
                print(f"{usuario.nombre}, selecciona tus cartas para el mazo.")
                while len(usuario.mazo.cartas) < 8: #mostrar mensaje cuando el mazo esta completo
                    print("Cartas disponibles:")
                    for i, carta in enumerate(cartas, 1): #muestra cartas guardadas en la base de datos
                        print(f"{i}. {carta}")
                    seleccion = int(input("Seleccione el número de la carta que desea agregar: ")) - 1
                    if 0 <= seleccion < len(cartas): # si esta entra las opciones la guarda, sino muestra mensaje
                        carta_elegida = cartas[seleccion]
                        if usuario.elegir_mazo(carta_elegida):
                           print(f"{usuario.nombre} ha agregado {carta_elegida.nombre} al mazo.")
                        else:
                            print(f"{usuario.nombre} ya tiene {carta_elegida.nombre} en su mazo.")
                    else:
                        print("Selección no válida. Intente de nuevo.")
            elif opcion == 2: # editar mazo
                while True: # el while es para que no salga del menu cuando ya realiza una accion 
                    print('Mazo de cartas: ')
                    for i, carta in enumerate(usuario.mazo.cartas, 1):
                        print(f"{i}. {carta}")
                    menu_mazo()
                    opcion = int(input("Seleccione una opción: "))
                    if opcion == 1:
                        if len(usuario.mazo.cartas) < 8: # si el mazo esta completo muestra mensaje, sino agrega carta
                            for i, carta in enumerate(cartas, 1):
                                print(f"{i}. {carta}")
                            seleccion = int(input("Seleccione el número de la carta que desea agregar: ")) - 1
                            carta_seleccionada = cartas[seleccion]
                            usuario.mazo.add_carta(carta_seleccionada)
                            print('Se agrego la carta correctamente')
                        else:
                            print('Antes de agregar una carta debe quitar una.')
                    elif opcion == 2: # el mazo debe tener al menos una carta para poder eliminar una carta
                        if len(usuario.mazo.cartas) > 0:
                            for i, carta in enumerate(usuario.mazo.cartas, 1):
                                print(f"{i}. {carta}")
                            seleccion = int(input("Seleccione el número de la carta que desea quitar: ")) - 1
                            carta_seleccionada = usuario.mazo.cartas[seleccion]
                            usuario.mazo.remove_carta(carta_seleccionada)
                            print('Se quito la carta correctamente')
                        else:
                            print('Antes de quitar una carta debe agregar una.')
                    elif opcion == 3: # subir nivel de carta con las monedas que tiene el jugador
                        for i, carta in enumerate(usuario.mazo.cartas, 1):
                            print(f"{i}. {carta} - Nivel: {carta.nivel}")
                        opt_carta = int(input("Seleccione la carta que desea subir de nivel:")) - 1
                        carta_nivel_seleccionada = usuario.mazo.cartas[opt_carta]
                        print(usuario.subir_nivel(carta_nivel_seleccionada)) # llama a al metodo y muestre el return correspondiente
                    elif opcion == 4:
                        break
            elif opcion == 3:
               partida = Partida(usuario, usuario_2)
               partida.iniciar_partida()
            elif opcion == 4:
               print("Saliendo...")
               break
    elif opcion == 2:
        print("Saliendo...")
        break