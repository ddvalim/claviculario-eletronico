from Abstracts.AbsctractTela import AbstractTela

from PySimpleGUI import Window, Input, Text, Button

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