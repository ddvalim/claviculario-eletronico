class FuncionarioNaoExisteException(Exception):
    def __init__(self):
        super().__init__('Funcionário com esta matrícula não existe')