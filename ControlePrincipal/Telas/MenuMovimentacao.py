from PySimpleGUI import Text, Window, Button
from Abstracts.AbsctractTela import AbstractTela

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
