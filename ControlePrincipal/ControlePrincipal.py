from Veiculo.ControleVeiculo import ControleVeiculo
from Funcionario.ControleFuncionarios import ControleFuncionarios
from MovimentoVeiculo.ControleMovimentacao import ControleMovimentacao
from ControlePrincipal.TelaPrincipal import TelaPrincipal

class ControlePrincipal:

    def __init__(self):
        self.__controle_veiculo = ControleVeiculo()
        self.__controle_funcionario = ControleFuncionarios(self.__controle_veiculo)
        self.__controle_movimentacao = ControleMovimentacao(self.__controle_veiculo, self.__controle_funcionario)

    def inicializar(self):
        while True:
            tela_principal = TelaPrincipal()
            opcao, xableize = tela_principal.show()
            tela_principal.close()
            print(opcao)
            if opcao != '0' and opcao != '1' and opcao != '2':
                exit()
            else:
                if opcao == '0':
                    print('*' * 30)
                    print('0 - Adicionar funcionário')
                    print('1 - Remover funcionário')
                    print('2 - Atualizar funcionário')
                    print('3 - Obter funcionários cadastrados')
                    print('4 - Detalhes do funcionário')
                    print('5 - Adicionar veículo à funcionário')
                    print('6 - Remover veículo de funcionário')
                    print('Outro caracter - voltar ao menu principal')
                    print('*' * 30)
            
                    reopcao = None

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
                    print('*' * 30)
                    print('0 - Listar veículos cadastrados')
                    print('1 - Adicionar veículo')
                    print('2 - Detalhes do veiculo')
                    print('3 - Remover veículo')
                    print('4 - Atualizar veículo')
                    print('Outro caracter - voltar ao menu principal')
                    print('*' * 30)
            
                    reopcao = None

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
        