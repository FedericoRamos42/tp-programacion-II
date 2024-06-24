from mazo import Mazo
from datos import cartas
class Jugador():
    def __init__(self, nombre:str, nivel:int, cantidad_trofeo:int):
        self.__nivel = nivel
        self.__cantidad_trofeo = cantidad_trofeo
        self.__mazo = Mazo()
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre:str) -> None:
        self.__nombre = nuevo_nombre
        
    @property
    def nivel(self) -> int:
        return self.__nivel
    
    @nivel.setter
    def nivel(self, nuevo_nivel:int) -> None:
        self.__nivel = nuevo_nivel
    
    @property
    def cantidad_trofeo(self) -> int:
        return self.__cantidad_trofeo
    
    @cantidad_trofeo.setter
    def cantidad_trofeo(self, nueva_cantidad_trofeo:int) -> None:
        self.__cantidad_trofeo = nueva_cantidad_trofeo
        
    @property
    def mazo(self) -> Mazo:
        return self.__mazo
    
    @mazo.setter
    def mazo(self, nuevo_mazo:Mazo) -> None:
        self.__mazo = nuevo_mazo
    
    def elegir_mazo(self) -> None:
        print(f"{self.nombre}, selecciona tus cartas para el mazo.")
        while len(self.mazo.cartas) < 8:
            print("Cartas disponibles:")
            for i, carta in enumerate(cartas, 1):
                print(f"{i}. {carta}")

            seleccion = int(input("Seleccione el número de la carta que desea agregar: ")) - 1
            if 0 <= seleccion < len(cartas):
                carta_elegida = cartas[seleccion]
                self.mazo.add_carta(carta_elegida)
                print(f"{carta_elegida.nombre} ha sido agregada a tu mazo.")
            else:
                print("Selección no válida. Intente de nuevo.")
        
    def jugar_carta(self) -> None:
        if not self.mazo.cartas:
            print(f"{self.nombre} no tiene cartas en su mazo para jugar.")
            return None

        print(f"{self.nombre}, selecciona una carta para jugar:")
        for i, carta in enumerate(self.mazo.cartas):
            print(f"{i + 1}. {carta}")

        seleccion = int(input("Seleccione el número de la carta que desea jugar: ")) - 1
        if 0 <= seleccion < len(self.mazo.cartas):
            carta_jugada = self.mazo.cartas.pop(seleccion)
            print(f"{self.nombre} ha jugado {carta_jugada.nombre}")
            return carta_jugada
        else:
            print("Selección no válida. Intente de nuevo.")
            return None
    
    