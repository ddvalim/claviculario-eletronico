class VeiculoJaRetiradoException(Exception):
    def __init__(self):
        self.motivo_negacao = 3
        super(Exception, self).__init__('Veiculo já foi retirado')