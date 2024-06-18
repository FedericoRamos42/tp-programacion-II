class Torre():
    def __init__(self, tipo_torre:str, daño_torre:int, vida_torre:int) -> None:
        self.__tipo_torre = tipo_torre
        self.__daño_torre = daño_torre
        self.__vida_torre = vida_torre
    
    @property
    def tipo_torre(self) -> str:
        return self.__tipo_torre
    
    @tipo_torre.setter
    def tipo_torre(self, nuevo_tipo_torre: str) -> None:
        self.__tipo_torre = nuevo_tipo_torre
    
    @property
    def daño_torre(self) -> int:
        return self.__daño_torre
    
    @daño_torre.setter
    def daño_torre(self, nuevo_daño_torre:int) -> None:
        self.__daño_torre = nuevo_daño_torre # hace falta setter?
        
    @property
    def vida_torre(self) -> int:
        return self.__vida_torre
    
    # hace falta setter de vida_torre?
    
    def atacar():
        pass
    
    def recibir_daño():
        pass