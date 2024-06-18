from jugador import Jugador

class Partida():
    def __init__(self, jugador_1:Jugador, jugador_2:Jugador) -> None:
        self.__jugador_1 = jugador_1
        self.__jugador_2 = jugador_2
        #tiempo de partida
    
    @property
    def jugador_1(self) -> Jugador:
        return self.__jugador_1
    
    @jugador_1.setter
    def jugador_1(self, nuevo_jugador_1:Jugador) -> None:
        self.__jugador_1 = nuevo_jugador_1
    
    @property
    def jugador_2(self) -> Jugador:
        return self.__jugador_2
    
    @jugador_2.setter
    def jugador_2(self, nuevo_jugador_2:Jugador) -> None:
        self.__jugador_2 = nuevo_jugador_2
    
    def iniciar_partida(self) -> None:
        pass