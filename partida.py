from jugador import Jugador
import time
import random

class Partida():
    DURACION_PARTIDA = 20
    def __init__(self, jugador_1:Jugador, jugador_2:Jugador) -> None:
        self.__jugador_1 = jugador_1
        self.__jugador_2 = jugador_2
        self.__tiempo_partida = Partida.DURACION_PARTIDA
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
    
    @property
    def tiempo_partida(self) -> int:
        return self.__tiempo_partida
    
    def iniciar_partida(self) -> None:
        # volver las torres al 100% de vida
        print("La partida ha comenzado!")
        while self.__tiempo_partida > 0:
            self.simular_turno()
            time.sleep(1)
            self.__tiempo_partida -= 1
            if self.partida_terminada():
                break
        self.mostrar_resultado()

    def simular_turno(self) -> None:
        dano_random = [40, 300, 24, 100, 53, 200]
        for torre in self.__jugador_1.torres:
            if not torre.esta_destruida():
                objetivo = random.choice(self.__jugador_2.torres)
                dano_torre_random_1 = random.choice(dano_random)
                objetivo.recibir_daño(dano_torre_random_1)
                objetivo.recibir_daño(random.choice(dano_random))
                print(f"{self.__jugador_1.nombre} ataca con {torre.tipo_torre} causando {dano_torre_random_1} de daño a una torre de {self.__jugador_2.nombre} que ahora tiene {objetivo.vida_torre} de vida")
                
        # Ataques del jugador 2 (computadora)
        for torre in self.__jugador_2.torres:
            if not torre.esta_destruida():
                objetivo = random.choice(self.__jugador_1.torres)
                dano_torre_random_2 = random.choice(dano_random)
                objetivo.recibir_daño(dano_torre_random_2)
                print(f"{self.__jugador_2.nombre} ataca con {torre.tipo_torre} causando {dano_torre_random_2} de daño a una torre de {self.__jugador_1.nombre} que ahora tiene {objetivo.vida_torre} de vida")
        
    def partida_terminada(self) -> bool:
    # Verificar si todas las torres del jugador 1 están destruidas
        torres_destruidas_jugador_1 = True
        for torre in self.__jugador_1.torres:
            if not torre.esta_destruida():
                torres_destruidas_jugador_1 = False
                break

    # Verificar si todas las torres del jugador 2 están destruidas
        torres_destruidas_jugador_2 = True
        for torre in self.__jugador_2.torres:
            if not torre.esta_destruida():
                torres_destruidas_jugador_2 = False
                break

    # Si todas las torres de cualquier jugador están destruidas, la partida ha terminado
        if torres_destruidas_jugador_1 or torres_destruidas_jugador_2:
            return True
        else:
            return False

    
    def mostrar_resultado(self) -> None:
        if all(torre.esta_destruida() for torre in self.__jugador_1.torres):
            print(f"{self.__jugador_2.nombre} ha ganado la partida!")
        elif all(torre.esta_destruida() for torre in self.__jugador_2.torres):
            print(f"{self.__jugador_1.nombre} ha ganado la partida!")
        else:
            print("La partida ha terminado en empate.")
