from Veiculo.ControleVeiculo import ControleVeiculo
from Funcionario.ControleFuncionarios import ControleFuncionarios
from MovimentoVeiculo.ControleMovimentacao import ControleMovimentacao
from entradaInvalidaException import EntradaInvalidaException
from EOFError import EOFErrorException

class ControlePrincipal:

    def __init__(self):
        self.__controle_veiculo = ControleVeiculo()
        self.__controle_funcionario = ControleFuncionarios(self.__controle_veiculo)
        self.__controle_movimentacao = ControleMovimentacao(self.__controle_veiculo, self.__controle_funcionario)

    def inicializar(self):
        while True:
            try:
                print("Bem-vindo ao sistema de controle do uso de veículos pelos funcionários da empresa X")
                print('*' * 30)
                print('Selecione a ação que deseja tomar')
                print('*' * 30)
                print(' ')
                print('0 - Gerenciar funcionário')
                print('1 - Gerenciar veículos')
                print('2 - Gerenciar movimentações')

                opcao = input()

                if opcao != 0 and opcao != 1 and opcao != 2:
                    raise EntradaInvalidaException()
                else:
                    if opcao_selecionada == 0:
                        print('0 - Adicionar funcionário')
                        print('1 - Remover funcionário')
                        print('2 - Autenticar funcionário')
                        print('3 - Atualizar funcionário')
                        print('4 - Obter funcionários cadastrados')
                        print('5 - Adicionar veículo à funcionário')
                        print('6 - Remover veículo de funcionário')
                        print('7 - Bloquear funcionário')
                        print('8 - Adicionar funcionário')

                        reopcao = input()

                        if reopcao == 0:
                            adiciona_funcionario()
                        elif reopcao == 1:
                            deleta_funcionario()
                        elif reopcao == 2:
                            autentica_funcionario()
                        elif reopcao == 3:
                            atualiza_funcionario()
                        elif reopcao == 4:
                            funcionarios_cadastrados()
                        elif reopcao == 5:
                            adiciona_veiculo_funcionario()
                        elif reopcao == 6:
                            deleta_veiculo_funcionario()
                        elif reopcao == 7:
                            bloqueia_funcionario()
                        elif reopcao == 8:
                            adiciona_funcionario()
                        else:
                            raise EntradaInvalidaException()

                    elif opcao_selecionada == 1:
                        print('0 - Verificar veículo')
                        print('1 - Listar veículos cadastrados')
                        print('2 - Adicionar veículo')
                        print('3 - Remover veículo')
                        print('4 - Atualizar quilometragem de um veículo')
                        print('5 - Atualizar veículo')

                        reopcao = input()

                        if reopcao == 0:
                            verifica_veiculo()
                        elif reopcao == 1:
                            veiculos_cadastrados()
                        elif reopcao == 2:
                            adiciona_veiculo()
                        elif reopcao == 3:
                            deleta_veiculo()
                        elif reopcao == 4:
                            atualiza_km_veiculo()
                        elif reopcao == 5:
                            atualiza_veiculo()
                        else:
                            raise EntradaInvalidaException()

                    elif opcao_selecionada == 2:
                        print('0 - Filtrar movimentação')
                        print('1 - Obter relatório por tipo')
                        print('2 - Retirar veículo')
                        print('3 - Devolver veículo')

                        reopcao = input()

                        if reopcao == 0:
            
            
            
            except EOFError:
                raise EOFErrorException()

