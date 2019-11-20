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
        func = self.__tela_funcionarios.adiciona_funcionario()
        if func['matricula'] not in self.__funcionarios.keys():
            funcionario = Funcionario(**func)
            self.__funcionarios[funcionario.matricula] = funcionario
            self.__adiciona_ao_banco()
        else:
            self.__tela_funcionarios.excecao('Já existe um funcionário com essa matrícula')

    def __adiciona_ao_banco(self):
        pickle.dump(self.__funcionarios, open('funcionarios.pkl', 'wb'))

    def autentica_funcionario(self):
        invalid = True
        while invalid:
            matricula = self.__tela_funcionarios.autentica_funcionario()
            try:
                matricula = int(matricula)
                invalid = False
            except ValueError:
                return self.__tela_funcionarios.excecao(str(EntradaInvalidaException()))
        return self.__funcionarios[matricula] if matricula in self.__funcionarios.keys() else None

    def funcionarios_cadastrados(self):
        self.__tela_funcionarios.funcionarios_cadastrados(self.__funcionarios.values())

    def atualiza_funcionario(self):
        func = self.autentica_funcionario()
        dict_func = self.__tela_funcionarios.atualiza_funcionario(func)
        for k,v in dict_func.items():
            setattr(func, k, v)
        self.__funcionarios[func.matricula] = func
        self.__adiciona_ao_banco()
        self.__tela_funcionarios.sucesso('atualização de funcionário')

    def deleta_funcionario(self):
        func = self.autentica_funcionario()
        if func is not None and 's' in self.__tela_funcionarios.confirmacao(f'Tem certeza que deseja exclui o funcionário com matrícula :{func.matricula}')[0].lower():
            del self.__funcionarios[func.matricula]
            self.__adiciona_ao_banco()
            self.__tela_funcionarios.sucesso('deleção de funcionário')

    def bloqueia_funcionario(self, matricula):
        func = self.__funcionarios[matricula]
        func.bloqueado = True
        self.__funcionarios[matricula] = func
        self.__adiciona_ao_banco()

    def adiciona_veiculo_funcionario(self):
        func = self.autentica_funcionario()
        if func is None:
            return self.excecao('Não existe funcionário com essa matrícula')
        veiculo = self.__controle_veiculo.verifica_veiculo()
        if veiculo is None:
            return self.excecao('Não existe veiculo com essa placa')
        func.adiciona_veiculo_cadastrado(veiculo)
        self.__adiciona_ao_banco()
        self.__tela_funcionarios.sucesso('adição de veiculo ao funcionário')

    def deleta_veiculo_funcionario(self):
        func = self.autentica_funcionario()
        veiculo = self.__controle_veiculo.verifica_veiculo()
        func.remove_veiculo_cadastrado(veiculo)
        self.__adiciona_ao_banco()
        self.__tela_funcionarios.sucesso('deleção de veiculo ao funcionário')

    def detalhes_do_funcionario(self):
        func = self.autentica_funcionario()
        self.__tela_funcionarios.detalhes_do_funcionario(func)
