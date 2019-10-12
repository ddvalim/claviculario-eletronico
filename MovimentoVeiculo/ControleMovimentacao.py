import pickle
import os

from .MovimentoVeiculo import MovimentoVeiculo
from .TelaMovimentacoes import TelaMovimentacoes

class ControleMovimentacao():
    def __init__(self, controle_veiculo, controle_funcionarios):
        self.__controle_funcionarios = controle_funcionarios
        self.__controle_veiculo = controle_veiculo
        self.__tela_movimentacoes = TelaMovimentacoes()
        if os.path.isfile('movimentacoes.pkl'):
            self.__movimentacoes = pickle.load(open('movimentacoes.pkl', 'rb'))
        else: 
            self.__movimentacoes = []
        self.__acessos_negados = []
        self.__acessos_permitidos = []
        for movimentacao in self.__movimentacoes:
            if movimentacao.motivo_negacao is not None:
                self.__acessos_negados.append(movimentacao)
            else:
                self.__acessos_permitidos.append(movimentacao)
    
    def retira_veiculo(self):
        try:
            funcionario = self.__controle_funcionarios.autentica_funcionario()   
            if funcionario.bloqueado == True:
                raise Exception() 
            veiculo = None
            veiculo = self.__controle_veiculo.verifica_veiculo('')
            if funcionario.cargo != 'diretoria':
                if veiculo not in funcionario.veiculos_cadastrados:
                    raise Exception('Veiculo invalido')
            retiradas = []
            devolucoes = [] 
            for moviment in self.__movimentacoes:
                if moviment.veiculo == veiculo:
                    if moviment.tipo == 0:
                        retiradas.append(moviment)
                    else:
                        devolucoes.append(moviment)
            if len(devolucoes) != len(retiradas):
                raise Exception('Carro já retirado')
        except ex as ex:
            func_negados = []
            for movimentacao in self.__acessos_negados:
                if movimentacao.funcionario == funcionario:
                    func_negados.append(movimentacao)
            if len(func_negados) == 3:
                self.__controle_funcionarios.bloqueia_usuario(funcionario.matricula)
            mov = MovimentoVeiculo(veiculo, funcionario, 0, ex.motivo_negacao)
            self.__acessos_negados.append(mov)
            self.__movimentacoes.append(mov)
            return self.__tela_movimentacoes.excecao(str(ex))    

        MovimentoVeiculo()
        
        