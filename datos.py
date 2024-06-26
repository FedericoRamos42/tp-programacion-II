from carta import Carta
from jugador import Jugador
cartas = [
    Carta("Caballero", "Tropa", 3, 1),
    Carta("Arqueras", "Tropa", 3, 1),
    Carta("Gigante", "Tropa", 5, 1),
    Carta("Bola de Fuego", "Hechizo", 4, 1),
    Carta("Descarga", "Hechizo", 2, 1),
    Carta("Mosquetera", "Tropa", 4, 1),
    Carta("Bebé Dragón", "Tropa", 4, 1),
    Carta("P.E.K.K.A", "Tropa", 7, 1),
    Carta("Príncipe", "Tropa", 5, 1),
    Carta("Mini P.E.K.K.A", "Tropa", 4, 1),
    Carta("Ejército de Esqueletos", "Tropa", 3, 1),
    Carta("Bruja", "Tropa", 5, 1),
    Carta("Montapuercos", "Tropa", 4, 1),
    Carta("Esqueleto Gigante", "Tropa", 6, 1),
    Carta("Barril de Duendes", "Hechizo", 3, 1),
    Carta("Valquiria", "Tropa", 4, 1),
    Carta("Tesla", "Estructura", 4, 1),
    Carta("Cañón", "Estructura", 3, 1),
    Carta("Lanzarrocas", "Tropa", 5, 1),
]

jugadores = [
   Jugador("joaquin", "123", 2, 4, 500),
   Jugador("juan", "123", 2, 4, 400),
   Jugador("pedro", "123", 2, 4, 600),
   Jugador("maria", "123", 2, 4, 300),
   Jugador("jose", "123", 2, 4, 200),
   Jugador("ana", "123", 2, 4, 1200),
   Jugador("luis", "123", 2, 4, 400),
]


usuario_2 = Jugador("jose", "123", 2, 4, 200)

cartas_2 = [
    Carta("Bruja", "Tropa", 5, 1),
    Carta("Montapuercos", "Tropa", 4, 1),
    Carta("Esqueleto Gigante", "Tropa", 6, 1),
    Carta("Barril de Duendes", "Hechizo", 3, 1),
    Carta("Valquiria", "Tropa", 4, 1),
    Carta("Tesla", "Estructura", 4, 1),
    Carta("Cañón", "Estructura", 3, 1),
    Carta("Lanzarrocas", "Tropa", 5, 1),
]

for carta in cartas_2 :
    usuario_2.mazo.add_carta(carta)