from jugador import Jugador
import time
import random

class Partida():
    DURACION_PARTIDA = 40
    
    def __init__(self, jugador_1:Jugador, jugador_2:Jugador) -> None:
        self.__jugador_1 = jugador_1
        self.__jugador_2 = jugador_2
        self.__tiempo_partida = Partida.DURACION_PARTIDA
    
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
    
    @property
    def tiempo_partida(self) -> int:
        return self.__tiempo_partida
    
    def iniciar_partida(self) -> None:
        while self.__tiempo_partida > 0:
            self.simular_turno()
            time.sleep(1)
            self.__tiempo_partida -= 1
            if self.partida_terminada():
                break
        self.mostrar_resultado()

    def simular_turno(self) -> None:
        dano_random = [40, 300, 24, 100, 53, 200]
        
        torres_atacantes_jugador_1 = [torre for torre in self.__jugador_1.torres if not torre.esta_destruida()]
        torres_objetivo_jugador_2 = [torre for torre in self.__jugador_2.torres if not torre.esta_destruida()]
        
        if torres_atacantes_jugador_1 and torres_objetivo_jugador_2:
            carta_azar_1 = random.choice(self.jugador_1.mazo.cartas)
            objetivo_2 = random.choice(torres_objetivo_jugador_2)
            dano_torre_random_1 = random.choice(dano_random)
            objetivo_2.recibir_daño(dano_torre_random_1)
            print(f"{self.__jugador_1.nombre} ataca la torre {objetivo_2.tipo_torre} con la carta {carta_azar_1} y le causa un daño de {dano_torre_random_1} a una torre, que ahora tiene {objetivo_2.vida_torre} de vida")

        torres_atacantes_jugador_2 = [torre for torre in self.__jugador_2.torres if not torre.esta_destruida()]
        torres_objetivo_jugador_1 = [torre for torre in self.__jugador_1.torres if not torre.esta_destruida()]
        
        if torres_atacantes_jugador_2 and torres_objetivo_jugador_1:
            carta_azar_2 = random.choice(self.jugador_2.mazo.cartas)
            objetivo_1 = random.choice(torres_objetivo_jugador_1)
            dano_torre_random_2 = random.choice(dano_random)
            objetivo_1.recibir_daño(dano_torre_random_2)
            print(f"{self.__jugador_2.nombre} ataca la torre {objetivo_1.tipo_torre} con la carta {carta_azar_2} y le causa un daño de {dano_torre_random_2} a una torre, que ahora tiene {objetivo_1.vida_torre} de vida")
        
    def partida_terminada(self) -> bool:
        torres_destruidas_jugador_1 = True #simula jugador logueado
        for torre in self.__jugador_1.torres:
            if not torre.esta_destruida():
                torres_destruidas_jugador_1 = False
                break

        torres_destruidas_jugador_2 = True # simula jugador por computadora
        for torre in self.__jugador_2.torres:
            if not torre.esta_destruida():
                torres_destruidas_jugador_2 = False
                break

        if torres_destruidas_jugador_1 or torres_destruidas_jugador_2:
            return True
        else:
            return False


    def mostrar_resultado(self) -> None:
        torres_destruidas_jugador_1 = True
        for torre in self.__jugador_1.torres:
            if not torre.esta_destruida():
                torres_destruidas_jugador_1 = False
                break

        torres_destruidas_jugador_2 = True
        for torre in self.__jugador_2.torres:
            if not torre.esta_destruida():
                torres_destruidas_jugador_2 = False
                break

        if torres_destruidas_jugador_1:
            self.__jugador_2.cantidad_trofeo += 1
            print(f"{self.__jugador_2.nombre} ha ganado la partida!")
            print(f'Ahora tiene {self.jugador_2.cantidad_trofeo} Trofeos')
        elif torres_destruidas_jugador_2:
            self.__jugador_1.cantidad_trofeo += 1
            print(f"{self.__jugador_1.nombre} ha ganado la partida!")
            print(f'Ahora tiene {self.jugador_1.cantidad_trofeo} Trofeos')
        else:
            print("La partida ha terminado en empate.")

