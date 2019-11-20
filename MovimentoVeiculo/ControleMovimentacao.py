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
    
    @property
    def acessos_negados(self):
        neg = []
        for movimentacao in self.__movimentacoes:
            if movimentacao.motivo_negacao is not None:
                neg.append(movimentacao)
        return neg
    
    @property
    def acessos_permitidos(self):
        per = []
        for movimentacao in self.__movimentacoes:
            if movimentacao.motivo_negacao is None:
                per.append(movimentacao)
        return per
        

    def __adiciona_ao_banco(self):
        pickle.dump(self.__movimentacoes, open('movimentacoes.pkl', 'wb'))

    def retira_veiculo(self):
        try:
            funcionario = self.__controle_funcionarios.autentica_funcionario()   
            veiculo = None
            if funcionario is None:
                    self.__tela_movimentacoes.excecao('Funcionario com essa matrícula não foi achado')
                    return
            if funcionario.bloqueado == True:
                raise FuncionarioBloqueadoException()
            veiculo = self.__controle_veiculo.verifica_veiculo()
            if veiculo is None:
                self.__tela_movimentacoes.excecao('Veiculo com essa placa não foi achado')
                return
            if funcionario.cargo != 'diretoria':
                if veiculo.placa not in funcionario.placas_veiculos():
                    raise VeiculoInvalidoException()
            retiradas = []
            devolucoes = [] 
            for moviment in self.__movimentacoes:
                if moviment.veiculo is not None and moviment.veiculo.placa == veiculo.placa and moviment.motivo_negacao is None:
                    if moviment.tipo == 0  :
                        retiradas.append(moviment)
                    else:
                        devolucoes.append(moviment)

            if len(devolucoes) != len(retiradas):
                raise VeiculoJaRetiradoException()
            else:
                mov = MovimentoVeiculo(veiculo=veiculo, funcionario=funcionario, tipo=0)
                self.__movimentacoes.append(mov)
                self.__adiciona_ao_banco()
                self.__tela_movimentacoes.sucesso('retirada de veículo')
        except Exception as ex:
            func_negados = []
            for movimentacao in self.acessos_negados:
                if movimentacao.funcionario.matricula == funcionario.matricula:
                    func_negados.append(movimentacao)
            if len(func_negados) >= 3 and funcionario.bloqueado == False:
                self.__controle_funcionarios.bloqueia_funcionario(funcionario.matricula)
            mov = MovimentoVeiculo(veiculo, funcionario, 0, ex.motivo_negacao)
            self.__movimentacoes.append(mov)
            self.__adiciona_ao_banco()
            return self.__tela_movimentacoes.excecao(str(ex))

    def devolve_veiculo(self):
        try:
            funcionario = self.__controle_funcionarios.autentica_funcionario()
            veiculo = None
            if funcionario is None:
                self.__tela_movimentacoes.excecao('Funcionario com essa matrícula não foi achado')
                return
            if funcionario.bloqueado == True:
                raise FuncionarioBloqueadoException()
            veiculo = self.__controle_veiculo.verifica_veiculo()
            if veiculo is None:
                self.__tela_movimentacoes.excecao('Veiculo com essa placa não foi achado')
                return
            retiradas = []
            devolucoes = []
            date_latest = datetime.datetime(1970, 1, 1)
            mov_latest = None
            for moviment in self.__movimentacoes:
                if moviment.veiculo is not None and moviment.veiculo.placa == veiculo.placa and moviment.motivo_negacao is None:
                    if date_latest < moviment.data:
                        date_latest = moviment.data
                        mov_latest = moviment
                    if moviment.tipo == 0:
                        retiradas.append(moviment)
                    else:
                        devolucoes.append(moviment)
            if len(devolucoes) == len(retiradas):
                raise VeiculoJaDevolvidoException()
            elif mov_latest.funcionario.matricula != funcionario.matricula:
                raise FuncionarioNaoRetirouETentouDevolverException()
            else:
                self.__controle_veiculo.atualiza_km(veiculo)
                mov = MovimentoVeiculo(veiculo=veiculo, funcionario=funcionario, tipo=1)
                self.__movimentacoes.append(mov)
                self.__adiciona_ao_banco()
                self.__tela_movimentacoes.sucesso('devolução de veículo')
        except Exception as ex:
            func_negados = []
            for movimentacao in self.acessos_negados:
                if movimentacao.funcionario.matricula == funcionario.matricula:
                    func_negados.append(movimentacao)
            if len(func_negados) >= 3 and funcionario.bloqueado == False:
                self.__controle_funcionarios.bloqueia_funcionario(funcionario.matricula)
            mov = MovimentoVeiculo(veiculo, funcionario, 1, ex.motivo_negacao)
            self.__movimentacoes.append(mov)
            self.__adiciona_ao_banco()
            return self.__tela_movimentacoes.excecao(str(ex))
    
    def acessos_por_tipo(self):
        tipo = self.__tela_movimentacoes.acessos_por_tipo()
        if tipo == '1':
            self.__tela_movimentacoes.relatorio(self.acessos_negados)
        elif tipo == '2':
            self.__tela_movimentacoes.relatorio(self.acessos_permitidos)
        else:
            self.__tela_movimentacoes.relatorio(self.__movimentacoes)
    
    def filtra_movimentacoes(self):
        filtros = self.__tela_movimentacoes.filtra_movimentacoes()
        movimentacoes = []
        if filtros is None:
            self.__tela_movimentacoes.relatorio(self.__movimentacoes)
        elif isinstance(filtros, dict):
            for mov in self.__movimentacoes:
                if mov.motivo_negacao == filtros[1]:
                    movimentacoes.append(mov) 
        elif filtros == 2:
            func = self.__controle_funcionarios.autentica_funcionario()
            if func is None:
                return self.__tela_movimentacoes.excecao('Não existe funcionário com essa matrícula')
            for mov in self.__movimentacoes:
                if mov.funcionario is not None and mov.funcionario.matricula == func.matricula:
                    movimentacoes.append(mov) 
        elif filtros == 3:
            veic = self.__controle_veiculo.verifica_veiculo()
            if veic is None:
                return self.__tela_movimentacoes.excecao('Não existe veiculo com essa placa')
            for mov in self.__movimentacoes:
                if mov.veiculo is not None and mov.veiculo.placa == veic.placa:
                    movimentacoes.append(mov)
        self.__tela_movimentacoes.relatorio(movimentacoes) 
            