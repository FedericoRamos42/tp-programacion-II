from carta import Carta

class Mazo():
    def __init__(self) -> None:
        self.__cartas = []
    
    @property
    def cartas(self) -> list[Carta]:
        return self.__cartas
    
    def add_carta(self, carta:Carta) -> None:
        self.__cartas.append(carta)
    
    def remove_carta(self, carta:Carta) -> None:
        self.__cartas.remove(carta)
    