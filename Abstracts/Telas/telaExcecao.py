import PySimpleGUI as sg

from Abstracts.AbsctractTela import AbstractTela

class TelaExcecao(AbstractTela):
    def __init__(self, message):
        layout = [
            [sg.Text('Ocorreu uma exceção ao executar o programa: ')],
            [sg.Text(message)],
            [sg.Button('Voltar')]
        ]
        self.window = sg.Window('Erro').layout(layout)
