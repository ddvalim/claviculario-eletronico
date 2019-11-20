import PySimpleGUI as sg
from Abstracts.abs_tela import AbstractTela
from .Veiculo import Veiculo
from Validators.Veiculo import validator
from .Telas import telaListaVeiculos, telaDetalhesVeiculo, telaVerificaVeiculo, telaAtualizaKm, telaAdicionaVeiculo


class telaVeiculo(AbstractTela):
    def __init__(self):
        self.__validator = validator

    def lista_veiculos(self, veiculos):
        tela_veiculo = telaListaVeiculos(veiculos)
        tela_veiculo.show()
        tela_veiculo.close()

    def detalhes_veiculo(self, veiculo):
        tela_detalhes = telaDetalhesVeiculo(veiculo)
        tela_detalhes.show()
        tela_detalhes.close()

    def adiciona_veiculo(self):
        veic = {}
        for k in self.__validator.keys():
            invalid = True
            represent = k if k != 'km' else 'kilometragem'
            while invalid:
                tela_adiciona_vel = telaAdicionaVeiculo(represent)
                botao, dicionario = tela_adiciona_vel.show()
                tela_adiciona_vel.close()
                inpu = dicionario['inpu']

                try:
                    inpu = self.__validator[k](inpu)
                except Exception:
                    self.excecao('Valor inválido para o campo')
                if isinstance(inpu, self.__validator[k]):
                    if self.__validator[k] == str:
                        if len(inpu) != 0:
                            invalid = False
                    else:
                        invalid = False
                    veic[k] = inpu
        return veic

    def verifica_veiculo(self):
        tela_verificacao = telaVerificaVeiculo()
        botao, detalhe = tela_verificacao.show()
        placa = detalhe[0]
        tela_verificacao.close()
        return placa

    def remove_veiculo(self, veiculo):
        a = self.confirmacao(f'Tem certeza que deseja deletar o veiculo -> {veiculo.placa}?')
        if a[0].lower() == 's':
            b = self.sucesso('Veículo deletado com sucesso')
        else:
            b = self.excecao('Ação cancelada')

    def atualiza_km(self):
        while True:
            tela_atualiza_km = telaAtualizaKm()
            _, km = tela_atualiza_km.show()
            try:
                return float(km)
            except ValueError:
                self.excecao('Valor inválido para kilometragem, tente novamente')

    def atualiza_veiculo(self, veiculo:Veiculo):        
        veic = {}
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
