from jugador import Jugador
from datos import *
from partida import Partida

def linea():
    print('-------------------------------')

def mostrar_cartas():
    for i, carta in enumerate(cartas, 1): 
        print(f"{i}. {carta} - Tipo de carta: {carta.tipo_carta} - Nivel: {carta.nivel}")
        

def menu_usuario_logeado(usuario:Jugador) -> None:
    
    while usuario: #devuelve true si el usuario existe, sino es false
            mostrar_menu() # Sub menu para cuando el usuario ya esta logueado
            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número.")
                continue
            linea()
            if opcion == 1: # Jugador arma su mazo
                print(f"{usuario.nombre}, selecciona tus cartas para el mazo.")
                while len(usuario.mazo.cartas) < 8: #mostrar mensaje cuando el mazo esta completo
                    linea()
                    print("Cartas disponibles:")
                    mostrar_cartas() # cartas guardadas en datos.py
                    try:
                        seleccion = int(input("Seleccione el número de la carta que desea agregar: ")) - 1
                    except ValueError:
                        print("Entrada no válida. Por favor ingrese un número.")
                        continue
                    if 0 <= seleccion < len(cartas): # si esta entre las opciones la guarda, sino muestra mensaje
                        carta_elegida = cartas[seleccion]
                        if usuario.elegir_mazo(carta_elegida):
                           print(f"{usuario.nombre} ha agregado {carta_elegida.nombre} al mazo.")
                        else:
                            print(f"{usuario.nombre} ya tiene {carta_elegida.nombre} en su mazo.")
                    else:
                        print("Selección no válida. Intente de nuevo.")
            elif opcion == 2: # editar mazo
                while True:
                    linea()
                    print('Mazo de cartas: ')
                    for i, carta in enumerate(usuario.mazo.cartas, 1):
                        print(f"{i}. {carta}")
                    linea()
                    menu_mazo()
                    try:
                        opcion_mazo = int(input("Seleccione una opción: "))
                    except ValueError:
                        print("Entrada no válida. Por favor ingrese un número.")
                        continue
                    if opcion_mazo == 1:
                        if len(usuario.mazo.cartas) < 8: # si el mazo esta completo muestra mensaje, sino agrega carta
                            mostrar_cartas()
                            try:
                                seleccion = int(input("Seleccione el número de la carta que desea agregar: ")) - 1
                            except ValueError:
                                print("Entrada no válida. Por favor ingrese un número.")
                                continue
                            carta_seleccionada = cartas[seleccion]
                            usuario.mazo.add_carta(carta_seleccionada)
                            print('Se agrego la carta correctamente')
                        else:
                            print('Antes de agregar una carta debe quitar una.')
                    elif opcion_mazo == 2:
                        if validar_mazo(usuario): # el mazo debe tener al menos una carta para poder eliminar una carta
                            for i, carta in enumerate(usuario.mazo.cartas, 1):
                                print(f"{i}. {carta}")
                            try:
                                seleccion = int(input("Seleccione el número de la carta que desea quitar: ")) - 1
                            except ValueError:
                                print("Entrada no válida. Por favor ingrese un número.")
                                continue
                            carta_seleccionada = usuario.mazo.cartas[seleccion]
                            usuario.mazo.remove_carta(carta_seleccionada)
                            print('Se quito la carta correctamente')
                        else:
                            print('Antes de quitar una carta debe agregar una.')
                    elif opcion_mazo == 3: # subir nivel de carta con las monedas que tiene el jugador
                        if validar_mazo(usuario): 
                            linea()
                            print(f'Monedas en la cuenta: {usuario.cantidad_monedas}')
                            linea()
                            print(f'Valor en monedas por nivel: ')
                            for j, valor in enumerate (valor_nivel, 1):
                                print(f'Nivel {j} - Costo: {valor}')
                            linea()
                            for i, carta in enumerate(usuario.mazo.cartas, 1):
                                print(f"{i}. {carta} - Nivel: {carta.nivel}")
                            try:
                                opt_carta = int(input("Seleccione la carta que desea subir de nivel:")) - 1
                            except ValueError:
                                print("Entrada no válida. Por favor ingrese un número.")
                                continue
                            carta_nivel_seleccionada = usuario.mazo.cartas[opt_carta]
                            linea()
                        
                            print(usuario.subir_nivel(carta_nivel_seleccionada))
                            linea()
                            print(f'La cantidad actual de monedas es: {usuario.cantidad_monedas}')
                        else:
                            print('No tiene cartas en su mazo.')
                    elif opcion_mazo == 4:
                        print("Cerrando edicion de mazo")
                        break
            elif opcion == 3:
                if len(usuario.mazo.cartas) == 8:
                    partida = Partida(usuario, usuario_2)
                    print(f"{usuario.nombre} inicia la partida contra {usuario_2.nombre}.")
                    partida.iniciar_partida()
                else:
                    print('Debe completar el mazo para comenzar la partida.')
            elif opcion == 4:
               print("Cerrando de sesión")
               break
           
def validar_mazo(usuario: Jugador) -> bool:
    if len(usuario.mazo.cartas) > 0:
        return True
    else:
        return False         

def login() -> Jugador:
    nombre_de_usuario = input("Ingrese su nombre: ")
    contrasena = input("Ingrese su contraseña: ")
    for usuario in jugadores:
        if usuario.nombre == nombre_de_usuario and usuario.contrasena == contrasena:
            linea()
            mostrar_datos_usuario(usuario)
            return usuario
    print(f"Usuario {nombre_de_usuario} no encontrado.")
    
def registrarse() -> Jugador:
    while True:
        try:
            nombre_de_usuario = input("Ingrese un nombre de usuario: ")
            contrasena = input("Ingrese una contraseña: ")
            jugador = Jugador(nombre_de_usuario, contrasena)
            jugadores.append(jugador)
            print(f"Usuario {nombre_de_usuario} registrado con éxito.")
            return jugador
        except Exception as error:
            print(error)
    

def mostrar_datos_usuario(usuario:Jugador) -> None:
    print(f'Bienvenido {usuario.nombre}')
    print(f'Trofeos: {usuario.cantidad_trofeo}')
    print(f'Nivel de cuenta: {usuario.nivel}')
    print(f'Cantidad de monedas de oro: {usuario.cantidad_monedas}')

def menu() -> None:
    print("1. Iniciar Sesion")
    print("2. Registrarse")
    print("3. Salir")
    
def mostrar_menu():
    linea()
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
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.")
        continue
    linea()
    if opcion == 1:
        usuario = login()
        menu_usuario_logeado(usuario)
    elif opcion == 2:
        usuario = registrarse()
        menu_usuario_logeado(usuario)
    elif opcion == 3:
        print("Saliendo...")
        break
