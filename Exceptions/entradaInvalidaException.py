class EntradaInvalidaException(Exception):
    def __init__(self):
        super().__init__("Dado de entrada inválido! Tente outra vez")