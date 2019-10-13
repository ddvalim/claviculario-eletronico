import pickle
import datetime
import os

from Exceptions.FuncionarioBloqueadoException import FuncionarioBloqueadoException
from Exceptions.VeiculoInvalidoException import VeiculoInvalidoException
from Exceptions.VeiculoJaDevolvidoException import VeiculoJaDevolvidoException
from Exceptions.VeiculoJaRetiradoException import VeiculoJaRetiradoException
from Exceptions.FuncionarioNaoRetirouETentouDevolverException import FuncionarioNaoRetirouETentouDevolverException
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
    

    def __adiciona_ao_banco(self):
        pickle.dump(self.__movimentacoes, open('movimentacoes.pkl', 'wb'))

    def retira_veiculo(self):
        try:
            funcionario = self.__controle_funcionarios.autentica_funcionario()   
            if funcionario.bloqueado == True:
                raise FuncionarioBloqueadoException()
            veiculo = None
            veiculo = self.__controle_veiculo.verifica_veiculo('')
            if funcionario.cargo != 'diretoria':
                if veiculo not in funcionario.veiculos_cadastrados:
                    raise VeiculoInvalidoException()
            retiradas = []
            devolucoes = [] 
            for moviment in self.__movimentacoes:
                if moviment.veiculo == veiculo:
                    if moviment.tipo == 0:
                        retiradas.append(moviment)
                    else:
                        devolucoes.append(moviment)
            if len(devolucoes) != len(retiradas):
                raise VeiculoJaRetiradoException()
            else:
                mov = MovimentoVeiculo(veiculo=veiculo, funcionario=funcionario, tipo=0)
                self.__acessos_permitidos.append(mov)
                self.__movimentacoes.append(mov)
                self.__adiciona_ao_banco()
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
            self.__adiciona_ao_banco()
            return self.__tela_movimentacoes.excecao(str(ex))

        def devolve_veiculo(self):
            try:
                funcionario = self.__controle_funcionarios.autentica_funcionario()   
                if funcionario.bloqueado == True:
                    raise FuncionarioBloqueadoException()
                veiculo = None
                veiculo = self.__controle_veiculo.verifica_veiculo('')
                retiradas = []
                devolucoes = [] 
                date_latest = datetime.date(1970, 1, 1)
                mov_latest = None
                for moviment in self.__movimentacoes:
                    if moviment.veiculo == veiculo:
                        if date_latest < moviment.data:
                            date_latest = moviment.data
                            mov_latest = moviment
                        if moviment.tipo == 0:
                            retiradas.append(moviment)
                        else:
                            devolucoes.append(moviment)
                if len(devolucoes) == len(retiradas):
                    raise VeiculoJaDevolvidoException()
                elif mov_latest.funcionario != funcionario:
                    raise FuncionarioNaoRetirouETentouDevolverException()
                else:
                    mov = MovimentoVeiculo(veiculo=veiculo, funcionario=funcionario, tipo=1)
                    self.__acessos_permitidos.append(mov)
                    self.__movimentacoes.append(mov)
                    self.__adiciona_ao_banco()
            except ex as ex:
                func_negados = []
                for movimentacao in self.__acessos_negados:
                    if movimentacao.funcionario == funcionario:
                        func_negados.append(movimentacao)
                if len(func_negados) == 3:
                    self.__controle_funcionarios.bloqueia_usuario(funcionario.matricula)
                mov = MovimentoVeiculo(veiculo, funcionario, 1, ex.motivo_negacao)
                self.__acessos_negados.append(mov)
                self.__movimentacoes.append(mov)
                self.__adiciona_ao_banco()
                return self.__tela_movimentacoes.excecao(str(ex))
        
        def filtra_movimentacoes(self):
            filtros = self.__tela_movimentacoes.filtra_movimentacoes()
            movimentacoes = []
            if filtros is None:
                self.__tela_movimentacoes.relatorio(self.__movimentacoes())
            elif isinstance(filtros, dict):
                for mov in self.__movimentacoes:
                    if mov.motivo_negacao == filtros[1]
                        movimentacoes.append(mov) 
            elif filtros == 2:
                func = self.__controle_funcionarios.autentica_funcionario()
                for mov in self.__movimentacoes:
                    if mov.funcionario == func:
                        movimentacoes.append(mov) 
            elif filtros == 3:
                veic = self.__controle_veiculos.verifica_veiculo()
                for mov in self.__movimentacoes:
                    if mov.veiculo == veic:
                        movimentacoes.append(mov)
            self.__tela_movimentacoes.relatorio(movimentacoes) 
                