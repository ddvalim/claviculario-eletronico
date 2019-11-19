import PySimpleGUI as sg
from Validators.Veiculo import validator
from Abstracts.AbsctractTela import AbstractTela

class telaListaVeiculos(AbstractTela):
    def __init__(self, veiculos):
        self.window = sg.Window('Listar veículos')
        layout_tela_vel = [
            [sg.Text('Lista de veículos cadastrados')],
            [sg.Text('*' * 30)],
        ]
        for veiculo in veiculos:
            layout_tela_vel.append(
                [sg.Text(f'placa: {veiculo.placa} - marca: {veiculo.marca} - modelo: {veiculo.modelo}\n')])
        layout_tela_vel.append([sg.Button('Voltar')])
        self.window.Layout(layout_tela_vel)