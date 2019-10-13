class VeiculoInvalidoException(Exception):
    def __init__(self):
        self.motivo_negacao = 2
        super(Exception, self).__init__('Veiculo não válido para este funcionário')
        