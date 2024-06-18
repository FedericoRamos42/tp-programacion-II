from mazo import Mazo

class Jugador():
    def __init__(self, nombre:str, nivel:int, cantidad_trofeo:int, mazo: Mazo) -> None:
        self.__nombre = nombre
        self.__nivel = nivel
        self.__cantidad_trofeo = cantidad_trofeo
        self.__mazo = mazo
    
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
        
    def jugar_carta(self) -> None:
        pass
    
    