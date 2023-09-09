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

def solicitar_jugada_jugador(self):
    # 1. El sistema solicita al jugador que seleccione una jugada
    while True:
        jugada = input("¿Qué desea hacer? (h) para pedir carta, (p) para plantarse, (d) para doblar o (s) para rendirse: ")
        if jugada in ["h", "p", "d", "s"]:
            break
    # 2. Si el jugador pide una carta
    if jugada == "h":
        self.pedir_carta_jugador()
    # 3. Si el jugador se planta
    elif jugada == "p":
        self.plantarse_jugador()
    # 4. Si el jugador dobla
    elif jugada == "d":
        self.doblar_jugador()
    # 5. Si el jugador se rinde
    elif jugada == "s":
        self.rendirse_jugador()
def pedir_carta_jugador(self):
    # 3.1 El sistema le reparte una carta a la mano del jugador
    self.jugador.mano.append(self.mazo.pop())
    # 3.2 Si el valor de la mano del jugador es mayor a 21
    if self.jugador.valor_mano() > 21:
        self.finalizar_juego()
    # 3.3 Si el valor de la mano no supera 21
    else:
        self.solicitar_jugada_jugador()
def plantarse_jugador(self):
    # 4.1 Se calcular el valor de la mano, se muestra y se guarda
    self.jugador.calcular_valor_mano()
    # 4.2 Se ejecuta el requisito R4 hacer jugada de la casa
    self.hacer_jugada_casa()
def doblar_jugador(self):
    # 4.1 Se calcular el valor de la mano, se muestra y se guarda
    self.jugador.calcular_valor_mano()
    # 4.2 Se ejecuta el requisito R4 hacer jugada de la casa
    self.hacer_jugada_casa()
