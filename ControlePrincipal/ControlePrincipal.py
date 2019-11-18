from Veiculo.ControleVeiculo import ControleVeiculo
from Funcionario.ControleFuncionarios import ControleFuncionarios
from MovimentoVeiculo.ControleMovimentacao import ControleMovimentacao
from .TelaPrincipal import TelaPrincipal
from .Telas.MenuFuncionario import MenuFuncionario
from Veiculo.telaVeiculo import telaVeiculo


class ControlePrincipal:

    def __init__(self):
        self.__controle_veiculo = ControleVeiculo()
        self.__controle_funcionario = ControleFuncionarios(self.__controle_veiculo)
        self.__controle_movimentacao = ControleMovimentacao(self.__controle_veiculo, self.__controle_funcionario)

    def inicializar(self):
        while True:
            tela_principal = TelaPrincipal()
            tela_veiculo = telaVeiculo()
            menu_funcionario = MenuFuncionario()

            opcao, xableize = tela_principal.show()
            tela_principal.close()

            if opcao != '0' and opcao != '1' and opcao != '2':
                exit()
            else:
                if opcao == '0':
                    reopcao, _ = menu_funcionario.show()
                    menu_funcionario.close()

                    if reopcao == '0':
                        self.__controle_funcionario.adiciona_funcionario()
                    elif reopcao == '1':
                        self.__controle_funcionario.deleta_funcionario()
                    elif reopcao == '2':
                        self.__controle_funcionario.atualiza_funcionario()
                    elif reopcao == '3':
                        self.__controle_funcionario.funcionarios_cadastrados()
                    elif reopcao == '4':
                        self.__controle_funcionario.detalhes_do_funcionario()
                    elif reopcao == '5':
                        self.__controle_funcionario.adiciona_veiculo_funcionario()
                    elif reopcao == '6':
                        self.__controle_funcionario.deleta_veiculo_funcionario()

                elif opcao == '1':

                    reopcao, var2 = tela_veiculo.show()
                    tela_veiculo.close()

                    if reopcao == '0':
                        self.__controle_veiculo.lista_veiculos()
                    elif reopcao == '1':
                        self.__controle_veiculo.adiciona_veiculo()
                    elif reopcao == '2':
                        self.__controle_veiculo.detalhes_veiculo()
                    elif reopcao == '3':
                        self.__controle_veiculo.deleta_veiculo()
                    elif reopcao == '4':
                        self.__controle_veiculo.atualiza_veiculo()

                elif opcao == '2':
                    print('*' * 30)
                    print('0 - Filtrar movimentação')
                    print('1 - Obter relatório por tipo')
                    print('2 - Retirar veículo')
                    print('3 - Devolver veículo')
                    print('*' * 30)

                    reopcao = None

                    if reopcao == '0':
                        self.__controle_movimentacao.filtra_movimentacoes()
                    elif reopcao == '1':
                        self.__controle_movimentacao.acessos_por_tipo()
                    elif reopcao == '2':
                        self.__controle_movimentacao.retira_veiculo()
                    elif reopcao == '3':
                        self.__controle_movimentacao.devolve_veiculo()
        