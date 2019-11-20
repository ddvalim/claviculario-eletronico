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

class telaDetalhesVeiculo(AbstractTela):
    def __init__(self, veiculo):
        detalhes_vel = ''
        detalhes_vel += ((f'Veiculo - {veiculo.placa}\n'))
        detalhes_vel += ((f'Modelo: {veiculo.modelo}\n'))
        detalhes_vel += ((f'Marca: {veiculo.marca}\n'))
        detalhes_vel += ((f'Ano: {veiculo.ano}\n'))
        detalhes_vel += ((f'Kilometragem: {veiculo.km}'))

        layout_detalhes_vel2 = [
            [sg.Text('Detalhes do veículo:')],
            [sg.Text('*' * 15)],
            [sg.Text(detalhes_vel)],
            [sg.Button('Sair')]
        ]
        self.window = sg.Window('Detalhes do veículo')
        self.window.layout(layout_detalhes_vel2)

class telaVerificaVeiculo(AbstractTela):
    def __init__(self):
        self.window = sg.Window('Verificação de veículo')
        layout_detalhes_vel1 = [
            [sg.Text('Digite a placa do veículo:')],
            [sg.Input()],
            [sg.Button('Buscar')]
        ]
        self.window.Layout(layout_detalhes_vel1)

class telaAtualizaKm(AbstractTela):
    def __init__(self):
        self.window = sg.Window('Atualização de kilometragem')
        layout_atualiza_km = [
            [sg.Text('Informe a kilometragem rodada com o veículo:')],
            [sg.Text('Exemplo: 12.7')],
            [sg.Input()],
            [sg.Button('Atualizar')]
        ]
        self.window.Layout(layout_atualiza_km)