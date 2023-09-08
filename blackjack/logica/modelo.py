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
    def