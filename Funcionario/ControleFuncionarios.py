import pickle
import os

from .TelaFuncionarios import TelaFuncionarios
from .Funcionario import Funcionario

class ControleFuncionarios():
    def __init__(self, controle_veiculo):
        self.__controle_veiculo = controle_veiculo
        self.__tela_funcionarios = TelaFuncionarios()
        if os.path.isfile('funcionarios.pkl'):
            self.__funcionarios = pickle.load(open('funcionarios.pkl', 'rb'))
        else: 
            self.__funcionarios = {}
    
    def adiciona_funcionario(self):
        tela = self.__tela_funcionarios.adiciona_funcionario()
        if tela['matricula'] not in self.__funcionarios.keys():
            func = Funcionario(**tela)
        else:
            return self.__tela_funcionarios.excecao('Já existe um funcionário cadastrado com essa matrícula')
        self.__funcionarios[func.matricula] = Funcionario
        self.__adiciona_ao_banco()
    
    def __adiciona_ao_banco(self):
        pickle.dump(self.__funcionarios, open('funcionarios.pkl', 'wb'))