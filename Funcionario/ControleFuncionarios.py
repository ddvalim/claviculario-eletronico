from .TelaFuncionarios import TelaFuncionarios
from .Funcionario import Funcionario

class ControleFuncionarios():
    def __init__(self, controle_veiculo):
        self.__controle_veiculo = controle_veiculo
        self.__tela_funcionarios = TelaFuncionarios()
        self.__funcionarios = {}
    
    def adiciona_funcionario(self):
        Funcionario(**self.__tela_funcionarios.adiciona_funcionario())