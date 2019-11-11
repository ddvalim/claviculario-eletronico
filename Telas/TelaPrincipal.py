import PySimpleGUI as sg
from Abstracts.AbsctractTela import AbstractTela


class TelaPrincipal(AbstractTela):
    def __init__(self):
        layout = [
         [sg.Text('O que você quer fazer?')],
         [sg.Text('0 - Gerenciar funcionários', size=(15, 1)), sg.Button('0')],
         [sg.Text('1 - Gerenciar veículos', size=(15, 1)), sg.Button('1')],
         [sg.Text('2 - Gerenciar movimentações', size=(15, 1)), sg.Button('2')],
         [sg.Button('Sair')]
         ]
        self.__window = sg.Window('Claviculário Eletrônico').Layout(layout)

    @property
    def window(self):
        return self.__window
