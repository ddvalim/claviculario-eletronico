from Abstracts.abs_tela import AbstractTela
from ControleVeiculo import ControleVeiculo

class telaVeiculo(AbstractTela):
    def __init__(self):
        pass

    def lista_veiculos(self):
        print('*' * 30)
        print('Listando veículos...')
        print('*' * 30)

        for veiculo in veiculos_cadastrados:
            print(veiculo)

    def detalhes_veiculo(self, placa):
        if placa in veiculos_cadastrados.keys():
            vel = veiculos_cadastrados[placa]
            print(vel.modelo)
            print(vel.marca)
            print(vel.ano)
            print(vel.km)

    def adiciona_veiculo(self, veiculo:Veiculo):
        mensagem = 'Ocorreu um erro durante o cadastramento. Tente novamente.'
        print('*' * 30)
        print('Adicionando veículo...')
        print('*' * 30)

        print('Veículo cadastrado: ' + veiculo) if adiciona_veiculo(veiculo) == True else print(mensagem)

    def remove_veiculo(self, veiculo:Veiculo):
        mensagem = 'Ocorreu um erro durante o cadastramento. Tente novamente.'
        print("*" * 30)
        print('Removendo veículo...')
        print('*' * 30)

        print('Veículo removido: ' + veiculo) if deleta_veiculo(veiculo) == True else print(mensagem)

    def atualiza_veiculo(self, veiculo:Veiculo):
        mensagem = 'Ocorreu um erro durante o cadastramento. Tente novamente.'
        print('*' * 30)
        print('Atualizando veículo...')
        print('*' * 30)

        print('Veículo atualizado: ' + veiculo) if atualiza_veiculo(veiculo) == True else print(mensagem)

