from carta import Carta
from jugador import Jugador
cartas = [
    Carta("Caballero", "Tropa", 1),
    Carta("Arqueras", "Tropa", 1),
    Carta("Gigante", "Tropa", 1),
    Carta("Bola de Fuego", "Hechizo", 1),
    Carta("Descarga", "Hechizo", 1),
    Carta("Mosquetera", "Tropa", 1),
    Carta("Bebé Dragón", "Tropa", 1),
    Carta("P.E.K.K.A", "Tropa", 1),
    Carta("Príncipe", "Tropa", 1),
    Carta("Mini P.E.K.K.A", "Tropa", 1),
    Carta("Ejército de Esqueletos", "Tropa", 1),
    Carta("Bruja", "Tropa", 1),
    Carta("Montapuercos", "Tropa", 1),
    Carta("Esqueleto Gigante", "Tropa", 1),
    Carta("Barril de Duendes", "Hechizo", 1),
    Carta("Valquiria", "Tropa", 1),
    Carta("Tesla", "Estructura", 1),
    Carta("Cañón", "Estructura", 1),
    Carta("Lanzarrocas", "Tropa", 1),
]

jugadores = [
   Jugador("joaquin", "123", 5, 2, 500),
   Jugador("juan", "123", 24, 1, 400),
   Jugador("pedro", "123", 4, 4, 600),
   Jugador("maria", "123", 32, 6, 300),
   Jugador("jose", "123", 6, 12, 200),
   Jugador("ana", "123", 1, 3, 1200),
   Jugador("luis", "123", 24, 0, 400),
]


usuario_2 = Jugador("federico", "123", 44, 4, 200)

cartas_2 = [
    Carta("Bruja", "Tropa", 1),
    Carta("Montapuercos", "Tropa", 1),
    Carta("Esqueleto Gigante", "Tropa", 1),
    Carta("Barril de Duendes", "Hechizo", 1),
    Carta("Valquiria", "Tropa", 1),
    Carta("Tesla", "Estructura", 1),
    Carta("Cañón", "Estructura", 1),
    Carta("Lanzarrocas", "Tropa", 1),
]

valor_nivel = [
    50,
    100,
    200,
    400,
    800
]

for carta in cartas_2 :
    usuario_2.mazo.add_carta(carta)