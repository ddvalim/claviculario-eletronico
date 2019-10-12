from Veiculo.ControleVeiculo import ControleVeiculo
from Funcionario.ControleFuncionarios import ControleFuncionarios

class ControlePrincipal():
    def __init__(self):
        self.__controle_veiculo = ControleVeiculo()
        self.__controle_funcionario = ControleFuncionarios(self.__controle_veiculo)
    
    def adiciona_funcionario(self):
        self.__controle_funcionario.adiciona_funcionario()

    def adiciona_veiculo(self):
        self.__controle_veiculo.adiciona_veiculo(None)
    
    def lista_funcionarios(self):
        self.__controle_funcionario.funcionarios_cadastrados()

    # def lista_veiculos(self):
    #     self.__controle_veiculo.veiculos_cadastrados()
    
    def edita_funcionario(self):
        self.__controle_funcionario.atualiza_funcionario()

    def edita_veiculo(self):
        self.__controle_veiculo.atualiza_veiculo('',None)

    def deleta_funcionario(self):
        self.__controle_funcionario.deleta_funcionario()

    def deleta_veiculo(self):
        self.__controle_veiculo.deleta_veiculo(None)