from barco import Barco

class Tablero():
    def __init__(self,tablero:list[list],barcos:list[Barco]) -> None:
        self.__tablero = tablero
        self.__barcos = barcos
    
    @property
    def tablero(self):
        return self.__tablero
    @property
    def barcos(self):
        return self.__barcos
    