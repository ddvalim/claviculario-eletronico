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
            [sg.Text('*'*30)],
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
            b = self.excecao('Ação cancelada')

    def atualiza_km(self):
        #Eh preciso implementar uma tela aqui?
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
                    layout_atualiza_vel = [[sg.Text(f'{represent} do veiculo : {getattr(veiculo, k)}')]]
                    layout_atualiza_vel.append([sg.Text(f'Informe o/a {represent} do veiculo:')])
                    inpu = [sg.Input()]
                    button = [sg.Button('Atualizar'), sg.Button('Manter')]
                    layout_atualiza_vel.append(inpu)
                    layout_atualiza_vel.append(button)
                    janela = sg.Window('Atualiza veículo').layout(layout_atualiza_vel)
                    janela.Read()
                    janela.Close()

                    if button[0] != 'Manter':
                        try:
                            inpu = self.__validator[k](inpu)
                        except Exception:
                            invalido = [sg.Text('Valor invalido para o campo')]
                            layout_atualiza_vel.append(invalido)
                            janela.Read()
                            janela.Close()
                        if isinstance(inpu, self.__validator[k]):  
                            if self.__validator[k] == str:
                                if len(inpu) != 0:
                                    invalid = False
                            else:
                                invalid = False
                            veic[k] = inpu
                    else:
                        invalid = False
                    #Quando ele chega no atributo ano ele entra em loop
                    #Não está registrando as alterações
                    #Não termina o processo
        return veic
