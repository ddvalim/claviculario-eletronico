import pickle
import os

from .Veiculo import Veiculo
from .telaVeiculo import telaVeiculo


class ControleVeiculo:

    def __init__(self):
        if os.path.isfile('veiculos.pkl'):
            self.__veiculos_cadastrados = pickle.load(open('veiculos.pkl', 'rb'))
        else: 
            self.__veiculos_cadastrados = {}    
        self.__tela_veiculo = telaVeiculo()

    # METODOS

    def detalhes_veiculo(self):
        veiculo = self.verifica_veiculo()
        if veiculo is None:
            return self.__tela_veiculo.excecao('Este veículo não existe')
        self.__tela_veiculo.detalhes_veiculo(veiculo)

    def lista_veiculos(self):
        self.__tela_veiculo.lista_veiculos(self.__veiculos_cadastrados.values())

    def __adiciona_ao_banco(self):
        pickle.dump(self.__veiculos_cadastrados, open('veiculos.pkl', 'wb'))

    def verifica_veiculo(self):
        placa = self.__tela_veiculo.verifica_veiculo()
        return self.__veiculos_cadastrados[placa] if placa in self.__veiculos_cadastrados.keys() else None

    def adiciona_veiculo(self):
        vec = self.__tela_veiculo.adiciona_veiculo
        placa = vec['placa']
        if placa not in self.__veiculos_cadastrados.keys():
            self.__veiculos_cadastrados[placa] = Veiculo(**vec)
            self.__adiciona_ao_banco()
            self.__tela_veiculo.sucesso('adição de veiculo')

    def atualiza_veiculo(self):
        veiculo = self.verifica_veiculo()
        if veiculo is None:
            self.__tela_veiculo.excecao('Veiculo com esta placa não foi encontrado')
            return
        dict_veic = self.__tela_veiculo.atualiza_veiculo(veiculo)
        for k,v in dict_veic.items():
            setattr(veiculo, k, v)
        self.__veiculos_cadastrados[veiculo.placa] = veiculo
        self.__adiciona_ao_banco()
        self.__tela_veiculo.sucesso('atualização de veiculo')

    def atualiza_km(self, veiculo):
        if veiculo is not None:
            km = self.__tela_veiculo.atualiza_km()
            veiculo.atualiza_km(km)
            self.__veiculos_cadastrados[veiculo.placa] == veiculo
            self.__adiciona_ao_banco()
        else: 
            self.__tela_veiculo.excecao('Veiculo com esta placa não foi encontrado')

    def deleta_veiculo(self):
        veiculo = self.verifica_veiculo()
        if veiculo is not None and self.__tela_veiculo.remove_veiculo(veiculo):
            del self.__veiculos_cadastrados[veiculo.placa]
            self.__tela_veiculo.sucesso('deleção de veiculo')

