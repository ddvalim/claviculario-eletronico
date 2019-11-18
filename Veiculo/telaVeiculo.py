import PySimpleGUI as sg
from Abstracts.abs_tela import AbstractTela
from .Veiculo import Veiculo
from Validators.Veiculo import validator


class telaVeiculo(AbstractTela):

    def __init__(self):
        self.__validator = validator
        layout = [
            [sg.Text('O que você quer fazer?')],
            [sg.Text('0 - Listar veículos cadastrados'), sg.Button('0')],
            [sg.Text('1 - Adicionar veículo'), sg.Button('1')],
            [sg.Text('2 - Detalhes do veiculo'), sg.Button('2')],
            [sg.Text('3 - Remover veículo'), sg.Button('3')],
            [sg.Text('4 - Atualizar veículo'), sg.Button('4')],
            [sg.Text('Outro caracter - voltar ao menu principal')],
            [sg.Button('Sair')]]
        self.__window = sg.Window('Veículos').Layout(layout)

    @property
    def show(self):
        return self.__window
    def close(self):
        self.__window.Close()

    def lista_veiculos(self, veiculos):
        layout_tela_vel = [
            [sg.Text('Lista de veículos cadastrados')],
            [sg.Text('*'*15)],
        ]
        for veiculo in veiculos:
            layout_tela_vel.append([sg.Text(f'placa: {veiculo.placa} - marca: {veiculo.marca} - modelo: {veiculo.modelo}\n')])
        layout_tela_vel.append([sg.Button('Sair')])

        tela_lista_vel = sg.Window('Lista Veículos').layout(layout_tela_vel)
        tela_lista_vel.Read()
        tela_lista_vel.Close()

    def detalhes_veiculo(self, veiculo):
        detalhes_vel = []
        detalhes_vel.append((f'Veiculo - {veiculo.placa}'))
        detalhes_vel.append((f'Modelo: {veiculo.modelo}'))
        detalhes_vel.append((f'Marca: {veiculo.marca}'))
        detalhes_vel.append((f'Ano: {veiculo.ano}'))
        detalhes_vel.append((f'Kilometragem: {veiculo.km}'))

        layout_detalhes_vel2 = [
            [sg.Text('Detalhes do veículo:')],
            [sg.Text('*'*15)],
            [sg.Text(detalhes_vel)],
            [sg.Button('Sair')]
        ]
        tela_detalhes_vel2 = sg.Window('Detalhes do veículo').layout(layout_detalhes_vel2)
        tela_detalhes_vel2.Read()
        tela_detalhes_vel2.Close()


    def adiciona_veiculo(self):
        print('*' * 30)
        print('Adicionando veículo...')
        print('*' * 30)
        veic = {}
        for k in self.__validator.keys():
            invalid = True
            represent = k if k != 'km' else 'kilometragem'
            while invalid:    
                print(f'Informe o/a {represent} do veiculo:')
                inpu = input()
                try:
                    inpu = self.__validator[k](inpu)
                except Exception:
                    print('valor inválido para o campo')
                if isinstance(inpu, self.__validator[k]):  
                    if self.__validator[k] == str:
                        if len(inpu) != 0:
                            invalid = False
                    else:
                        invalid = False
                    veic[k] = inpu
        return veic

    def verifica_veiculo(self):
        layout_detalhes_vel1 = [
            [sg.Text('Digite a placa do veículo:')],
            [sg.Input()],
            [sg.Button('Buscar')]
        ]
        tela_detalhes_vel1 = sg.Window('Detalhes do veículo').layout(layout_detalhes_vel1)
        botao, detalhe = tela_detalhes_vel1.Read()
        placa = detalhe[0]
        tela_detalhes_vel1.Close()
        return placa


    def remove_veiculo(self, veiculo):
        a = self.confirmacao(f'Tem certeza que deseja deletar o veiculo -> {veiculo.placa}?')
        if a[0].lower() == 's':
            b = self.sucesso('Veículo deletado com sucesso')
        else:
            None

    def atualiza_km(self):
        while True:
            print('*' * 30)
            print('Informe a kilometragem rodada do Veiculo: ')
            print('Ex: 12.7')
            print('*' * 30)
            val = input()
            try:
                return float(val)
            except ValueError:
                self.excecao('Valor inválido para kilometragem tente novamente')
        

    def atualiza_veiculo(self, veiculo:Veiculo):        
        veic = {}
        print('*' * 30)
        print('Atualizando veiculo...')
        print('*' * 30)
        for k in self.__validator.keys():
            if k != 'placa':
                invalid = True
                represent = k if k != 'km' else 'kilometragem'
                while invalid:
                    print(f'{represent} do veiculo : {getattr(veiculo, k)}')
                    print(f'Informe o/a {represent} do veiculo (aperte enter se não deseja mudar):')
                    inpu = input()
                    if inpu != '':
                        try:
                            inpu = self.__validator[k](inpu)
                        except Exception:
                            print('Valor invalido para o campo')
                        if isinstance(inpu, self.__validator[k]):  
                            if self.__validator[k] == str:
                                if len(inpu) != 0:
                                    invalid = False
                            else:
                                invalid = False
                            veic[k] = inpu
                    else:
                        invalid = False
        return veic
