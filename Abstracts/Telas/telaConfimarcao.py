import PySimpleGUI as sg
from Abstracts.AbsctractTela import AbstractTela

class telaConfirmacao(AbstractTela):
    def __init__(self, acao):
        layout = [
            [sg.Text('Você deseja concluir a seguinte ação?')],
            [sg.Text(acao)],
            [sg.Button('Sim', key='S'), sg.Button('Não', key='N')]
        ]
        self.window = sg.Window('Confirmar a ação').layout(layout)