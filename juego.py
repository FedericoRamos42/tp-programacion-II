from jugador import Jugador

class Juego():
    def __init__(self,jugador_1:Jugador,jugador_2:Jugador,jugador_actual:Jugador) -> None:
        self.__jugador_1 = jugador_1
        self.__jugador_2 = jugador_2
        self.__jugador_actual = jugador_actual
    
    @property
    def jugador_1(self):
        return self.__jugador_1
    
    @jugador_1.setter #Hace falta un set?
    def jugador_1(self,nuevo_jugador_1:Jugador):
        self.__jugador_1 = nuevo_jugador_1
    
    @property
    def jugador_2(self):
        return self.__jugador_2
    
    @jugador_2.setter #Hace falta un set?
    def jugador_2(self,nuevo_jugador_2:Jugador):
        self.__jugador_2 = nuevo_jugador_2 
    
    @property
    def jugador_actual(self):
        return self.__jugador_actual
    
    @jugador_actual.setter #Hace falta un set?
    def jugador_actual(self,nuevo_jugador_actual:Jugador):
        self.__jugador_actual = nuevo_jugador_actual              