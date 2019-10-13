class FuncionarioBloqueadoException(Exception):
    def __init__(self):
        self.motivo_negacao = 1
        super(Exception, self).__init__('Funcionário com essa matrícula está bloqueado')
        