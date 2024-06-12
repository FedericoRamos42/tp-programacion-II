from tablero import Tablero
from barco import Barco

class Jugador():
    def __init__(self,nombre:str,tablero_propio:Tablero,tablero_enemigo:Tablero,barcos:list[Barco]) -> None:
        self.__nombre = nombre
        self.__tablero_propio = tablero_propio
        self.__tablero_enemigo = tablero_enemigo
        self.__barcos = barcos
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre:str):
        self.__nombre = nuevo_nombre
    
    @property
    def tablero_propio(self):
        return self.__tablero_propio
    
    @tablero_propio.setter
    def tablero_propio(self,nuevo_tablero_propio:str):
        self.__tablero_propio = nuevo_tablero_propio
    
    @property
    def tablero_enemigo(self):
        return self.__tablero_enemigo
    
    @tablero_enemigo.setter
    def tablero_enemigo(self,nuevo_tablero_enemigo:str):
        self.__tablero_enemigo = nuevo_tablero_enemigo
        
    @property
    def barcos(self):
        return self.__barcos
    
    #set de barcos?
    