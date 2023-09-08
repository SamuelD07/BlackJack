class Carta:

    def __init__(self, pinta: str, valor: int):
        self.pinta: str = pinta
        self.valor: int = valor
        self.tapada: bool = False

class Mano:
    def __init__(self, cartas: tuple[Carta, Carta]):
        self.cartas: list[Carta] = []

    def es_blackjack(self) -> bool:
        pass

class Baraja:
    def __init__(self):
        self.cartas: list[Carta] = []

    def revolver(self):
        pass
    def repartir_carta(self):
        pass

class Jugador:
    def __init__(self, nombre: str, fichas: int):
        self.nombre: str = nombre
        self.fichas: int = fichas
        self.mano: Mano = None

    def inicializar_mano(self, cartas: tuple[Carta, Carta]):
        pass

class Casa:
    def __init__(self):
        self.mano: Mano = None

    def inicializar_mano(self, cartas: tuple[Carta, Carta]):
        pass

class Blackjack:
    def __init__(self):
        self.jugador: Jugador = None
        self.cupier: Casa = None
        self.baraja: Baraja = None