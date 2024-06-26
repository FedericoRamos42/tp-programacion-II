from mazo import Mazo
from carta import Carta
from torre import Torre
# from datos import cartas
class Jugador():
    
    __users = set()
    def __init__(self, nombre:str, contrasena:str, nivel:int = 1, cantidad_trofeo:int = 0, cantidad_monedas:int = 500):
        self.__nombre = Jugador.__validacion_usuario(nombre)
        self.__contrasena = contrasena
        self.__nivel = nivel
        self.__cantidad_trofeo = cantidad_trofeo
        self.__cantidad_monedas = cantidad_monedas
        self.__mazo = Mazo()
        self.__torres = [
            Torre("Escolta", 1000),
            Torre("Escolta", 1000),
            Torre("Principal", 2000)
        ]
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def contrasena(self) -> str:
        return self.__contrasena
    
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
    def cantidad_monedas(self) -> int:
        return self.__cantidad_monedas
    
    @cantidad_monedas.setter
    def cantidad_monedas(self, nueva_cantidad_monedas:int) -> None:
        self.__cantidad_monedas = nueva_cantidad_monedas
    
    @property
    def mazo(self) -> Mazo:
        return self.__mazo
    
    @property
    def torres(self) -> list:
        return self.__torres
    
    @mazo.setter
    def mazo(self, nuevo_mazo:Mazo) -> None:
        self.__mazo = nuevo_mazo
        
    @classmethod
    def __validacion_usuario(cls, nombre:str) -> str:
        if nombre in cls.__users:
            raise Exception("El nombre de usuario ya existe. Intente con otro.")
        cls.__users.add(nombre)
        return nombre
        
    
    def elegir_mazo(self,carta:Carta) -> bool:
        if not carta in self.mazo.cartas:
            self.__mazo.add_carta(carta)
            return True
        else:
            return False
        
    def subir_nivel(self, carta:Carta) -> str:
        if carta.nivel < 5:
            niveles = [50, 100, 200, 400, 800] # valores de monedas para cada nivel
            costo = niveles[carta.nivel - 1]
            if self.cantidad_monedas < costo:
                return f"No tienes suficientes monedas para el nivel {carta.nivel + 1}"
            else:
                self.cantidad_monedas -= costo
                carta.nivel += 1
                return f"Carta {carta.nombre} subió a nivel {carta.nivel}"
        else:
            return "Ya tienes el nivel máximo de la carta"
        
        
    def jugar_carta(self) -> None: # agregar lo de elixr
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
    
    