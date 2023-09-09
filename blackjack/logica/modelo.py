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
def rendirse_jugador(self):


    def hacer_jugada_casa(self):
        # 1. Se destapa la carta oculta de la casa
        self.casa.destapar_carta_oculta()
        # 2. Si la mano de la casa es blackjack
        if self.casa.es_blackjack():
            # 2.1 Se ejecuta el requisito R5 finalizar juego (la casa gana)
            self.finalizar_juego(True)
        # 3. Si la mano de la casa no es blackjack
        else:
            # 3.1 Si la mano de la casa es menor o igual que 16 y menor que la mano del jugador
            if self.casa.get_valor() <= 16 and self.casa.get_valor() < self.jugador.get_valor():
                # 3.1.1 Se reparte una carta a la mano de la casa
                self.casa.repartir_carta()
                # 3.1.2 Se calcula el valor de la mano se vuelve a evaluar (punto 3.1)
                self.hacer_jugada_casa()
            # 3.2 Si la mano de la casa es mayor a 16 y menor o igual a 21
            elif self.casa.get_valor() > 16 and self.casa.get_valor() <= 21:
                # 3.2.1 Se ejecuta el requisito R5 Finalizar juego
                self.finalizar_juego(False)
            # 3.3 Si la mano de la casa se pasó de 21
            elif self.casa.get_valor() > 21:
                # 3.3.1 Se ejecuta el requisito R5 Finalizar juego
                self.finalizar_juego(False)

def finalizar_juego(self, jugador_gano):
    # 1. Se comparan las manos del jugador y de la casa
    if self.jugador.get_valor() > self.casa.get_valor() or self.casa.get_valor() > 21:
        # 2. Si el jugador tiene blackjack, su mano es mayor que la mano de la casa o la mano de la casa superó 21
        # 2.1 El sistema anuncia el jugador como ganador
        print("El jugador ha ganado")
        # 2.2 Se doblan las fichas de la apuesta realizada
        self.jugador.doblar_fichas()
    elif self.casa.get_valor() > self.jugador.get_valor() or self.jugador.get_valor() > 21:
        # 3. Si la casa tiene blackjack, su mano es mayor que la mano del jugador o la mano del jugador superó 21
        # 3.1 El sistema anuncia que el jugador perdió
        print("El jugador ha perdido")
        # 3.3 Se restan las fichas de la apuesta de las fichas del jugador
        self.jugador.restar_fichas(self.apuesta)
    else:
        # 4. Si la mano del jugador y la mano de la casa tienen el mismo valor
        # 4.1 El sistema anuncia empate
        print("Empate")
        # 4.2 se devuelven las fichas apostadas al jugador
        self.jugador.devolver_fichas(self.apuesta)
    # 5. Si el usuario tiene fichas disponibles
    if self.jugador.get_fichas() > 0:
        # 5.1 Se presenta un menú con las opciones para iniciar un nuevo (R2) o salir de la aplicación
        print("¿Desea iniciar un nuevo juego (R2) o salir de la aplicación?")
        opcion = input()
        if opcion == "R2":
            # 5.1.1 Si el usuario elige iniciar un nuevo juego, se reinicia el juego
            self.reiniciar_juego()
        else:
            # 5.1.2 Si el usuario elige salir de la aplicación, se cierra la aplicación
            sys.exit()
    # 6. Si usuario no tiene fichas disponibles
    else:
        # 6.1 Se termina la aplicación
        print("El jugador no tiene fichas disponibles. Fin del juego.")
        sys.exit()