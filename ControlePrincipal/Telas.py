from PySimpleGUI import Text, Window, Button
from Abstracts.AbsctractTela import AbstractTela

from PySimpleGUI import Window, Input, Text, Button


class MenuFuncionario(AbstractTela):
    def __init__(self):
        self.window = Window('Menu Funcionários').layout(
            [
                [Text('O que você deseja fazer?')],
                [Text('Adicionar funcionário'), Button('0')],
                [Text('Remover funcionário'), Button('1')],
                [Text('Atualizar funcionário'), Button('2')],
                [Text('Obter funcionários cadastrados'), Button('3')],
                [Text('Detalhes do funcionário'), Button('4')],
                [Text('Adicionar veículo à funcionário'), Button('5')],
                [Text('Remover veículo de funcionário'), Button('6')],
                [Button('Voltar')]
            ]
        )


class MenuVeiculo(AbstractTela):
    def __init__(self):
        self.window = Window('Menu Veículo').layout(
            [
                [Text('O que você deseja fazer?')],
                [Text('0 - Listar veículos cadastrados'), Button('0')],
                [Text('1 - Adicionar veículo'), Button('1')],
                [Text('2 - Detalhes do veiculo'), Button('2')],
                [Text('3 - Remover veículo'), Button('3')],
                [Text('4 - Atualizar veículo'), Button('4')],
                [Button('Voltar')]
            ]
        )

        import PySimpleGUI as sg


class MenuPrincipal(AbstractTela):
    def __init__(self):
        layout = [
            [Text('O que você quer fazer?')],
            [Text('Gerenciar funcionários'), Button('0')],
            [Text('Gerenciar veículos'), Button('1')],
            [Text('Gerenciar movimentações'), Button('2')],
            [Button('Sair')]
        ]
        self.window = Window('Claviculário Eletrônico').Layout(layout)


class MenuMovimentacao(AbstractTela):
    def __init__(self):
        self.window = Window('Menu movimentações').layout(
            [
                [Text('O que você deseja fazer?')],
                [Text('Filtrar movimentação'), Button('0')],
                [Text('Obter relatório por tipo'), Button('1')],
                [Text('Retirar veículo'), Button('2')],
                [Text('Devolver veículo'), Button('3')],
                [Button('Voltar')]
            ]
        )
