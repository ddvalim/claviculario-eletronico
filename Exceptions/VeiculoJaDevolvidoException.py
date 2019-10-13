class VeiculoJaDevolvidoException(Exception):
    def __init__(self):
        self.motivo_negacao = 4
        super(Exception, self).__init__('Veiculo já foi devolvido')
        