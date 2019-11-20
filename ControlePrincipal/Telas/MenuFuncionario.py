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
