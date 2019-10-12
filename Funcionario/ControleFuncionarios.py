import pickle
import os

from Exceptions.entradaInvalidaException import EntradaInvalidaException
from Exceptions.FuncionarioNaoExisteException import FuncionarioNaoExisteException
from Exceptions.JaExisteFuncionarioComEssaMatriculaException import JaExisteFuncionarioComEssaMatriculaException
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
            raise JaExisteFuncionarioComEssaMatriculaException()
        self.__funcionarios[func.matricula] = func
        self.__adiciona_ao_banco()

    def __adiciona_ao_banco(self):
        pickle.dump(self.__funcionarios, open('funcionarios.pkl', 'wb'))

    def autentica_funcionario(self):
        invalid = True
        while invalid:
            matricula = self.__tela_funcionarios.autentica_funcionario()
            try:
                matricula = int(matricula)
            except ValueError:
                return self.__tela_funcionarios.excecao(str(EntradaInvalidaException()))
            else:
                invalid = False
        if matricula not in self.__funcionarios.keys():
            raise FuncionarioNaoExisteException()
        else: 
            return self.__funcionarios[matricula]

    def funcionarios_cadastrados(self):
        self.__tela_funcionarios.funcionarios_cadastrados(self.__funcionarios.values())

    def atualiza_funcionario(self):
        func = self.autentica_funcionario()
        dict_func = self.__tela_funcionarios.atualiza_funcionario(func)
        for k,v in dict_func.items():
            setattr(func, k, v)
        self.__funcionarios[func.matricula] = func
        self.__adiciona_ao_banco()

    def deleta_funcionario(self):
        func = self.autentica_funcionario()
        response = self.__tela_funcionarios.deleta_funcionario(func)
        if response:
            del self.__funcionarios[func.matricula]
        self.__adiciona_ao_banco()

    def bloqueia_funcionario(self, matricula):
        self.__funcionarios[matricula].bloqueado == True

    def adiciona_veiculo_funcionario(self):
        func = self.autentica_funcionario()
        veiculo = self.__controle_veiculo.verifica_veiculo('')
        func.adiciona_veiculo_cadastrado(veiculo)

    def deleta_veiculo_funcionario(self):
        func = self.autentica_funcionario()
        veiculo = self.__controle_veiculo.verifica_veiculo('')
        func.deleta_veiculo_cadastrado(veiculo)

    def detalhes_do_funcionario(self):
        func = self.autentica_funcionario()
        self.__tela_funcionarios.detalhes_do_funcionario(func)
