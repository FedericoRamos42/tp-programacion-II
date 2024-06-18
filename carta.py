class Carta():
    def __init__(self, nombre:str, tipo_carta:str, valor_elixir:int, nivel:int) -> None:
        self.__nombre = nombre
        self.__tipo_carta = tipo_carta
        self.__valor_elixir = valor_elixir
        self.__nivel = nivel
        
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre
    
    @property
    def tipo_carta(self) -> str:
        return self.__tipo_carta
    
    @tipo_carta.setter
    def tipo_carta(self, nuevo_tipo_carta: str) -> None:
        self.__tipo_carta = nuevo_tipo_carta
    
    @property
    def valor_elixir(self) -> int:
        return self.__valor_elixir
    
    @valor_elixir.setter
    def valor_elixir(self, nuevo_valor_elixir: int) -> None:
        self.__valor_elixir = nuevo_valor_elixir
    
    @property
    def nivel(self) -> int:
        return self.__nivel
    
    @nivel.setter
    def nivel(self, nuevo_nivel: int) -> None:
        self.__nivel = nuevo_nivel
    
    def subir_nivel(self) -> None:
        pass