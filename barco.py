class Barco():
    def __init__(self, nombre:str, tamaño:int) -> None:
        self.__nombre = nombre
        self.__tamaño = tamaño
        self.__posiciones: list[tuple[int,int]] = []
        self.__hundido = False #iniciarlo con un valor.
        