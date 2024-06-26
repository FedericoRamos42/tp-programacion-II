class Torre():
    def __init__(self, tipo_torre:str, vida_torre:int) -> None:
        self.__tipo_torre = tipo_torre
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
    @vida_torre.setter
    def vida_torre(self, nueva_vida_torre:int) -> None:
        self.__vida_torre = nueva_vida_torre
    
    def recibir_daño(self, daño_torre:int) -> None:
        self.__vida_torre = self.__vida_torre - daño_torre
        if self.__vida_torre < 0:
            self.__vida_torre = 0

    def esta_destruida(self) -> bool:
        if self.__vida_torre <= 0:
            return True
        else: 
            return False
        