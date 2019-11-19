from Abstracts.AbsctractTela import AbstractTela

from PySimpleGUI import Window, Input, Text, Button

class MenuFuncionario(AbstractTela):
    def __init__(self):
        self.window = Window('Menu Funcionários').layout(
            [
                [Text('O que você deseja fazer?')],
                [Text('0 - Adicionar funcionário'), Button('0')],
                [Text('1 - Remover funcionário'), Button('1')],
                [Text('2 - Atualizar funcionário'), Button('2')],
                [Text('3 - Obter funcionários cadastrados'), Button('3')],
                [Text('4 - Atualizar veículo'), Button('4')],
                [Text('5 - Adicionar veículo à funcionário'), Button('5')],
                [Text('6 - Remover veículo de funcionário'), Button('6')],
                [Button('Voltar')]
            ]
        )
