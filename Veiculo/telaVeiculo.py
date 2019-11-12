from Abstracts.abs_tela import AbstractTela
from .Veiculo import Veiculo
from Validators.Veiculo import validator

class telaVeiculo(AbstractTela):
    def __init__(self):
        self.__validator = validator

    def lista_veiculos(self, veiculos):
        print('*' * 30)
        print('Listando veículos...')
        print('*' * 30)

        for veiculo in veiculos:
            print(f'placa: {veiculo.placa} - marca: {veiculo.marca} - modelo: {veiculo.modelo}')
        print('\n'*5)
        print('Pressione enter para continuar:')
        input()

    def detalhes_veiculo(self, veiculo):
        print('*'*30)
        print(f'Veiculo - {veiculo.placa}')
        print(f'Modelo: {veiculo.modelo}')
        print(f'Marca: {veiculo.marca}')
        print(f'Ano: {veiculo.ano}')
        print(f'Kilometragem: {veiculo.km}')
        print('\n'*5)
        print('Pressione enter para continuar:')

        return input()

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
                    print('valor invalido para o campo')
                if isinstance(inpu, self.__validator[k]):  
                    if self.__validator[k] == str:
                        if len(inpu) != 0:
                            invalid = False
                    else:
                        invalid = False
                    veic[k] = inpu
        return veic

    def verifica_veiculo(self):
        print('*' * 30)
        print('Informe a placa do Veiculo')
        print('*' * 30)
        return input()

    def remove_veiculo(self, veiculo):
        print('*'*30)
        print(f'Tem certeza que deseja deletar o veiculo -> {veiculo.placa}?')
        print('s - sim, n - nao')
        return True if input().lower() == 's' else False
        
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
