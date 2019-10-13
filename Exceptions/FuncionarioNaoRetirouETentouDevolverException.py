class FuncionarioNaoRetirouETentouDevolverException(Exception):
    def __init__(self):
        self.motivo_negacao = 5
        super(Exception, self).__init__('Funcionário não retirou e tentou devolver um Veiculo')
        