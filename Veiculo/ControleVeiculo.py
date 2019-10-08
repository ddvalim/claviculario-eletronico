from Veiculo import Veiculo
# from telaVeiculo import telaVeiculo


class ControleVeiculo:

    def __init__(self):
        self.__veiculos_cadastrados = {}
        # self.__tela_veiculo = telaVeiculo

    # GETTERS

    @property
    def veiculos_cadastrados(self):
        return self.__veiculos_cadastrados

    # METODOS

    def verifica_veiculo(self, placa):
        return self.__veiculos_cadastrados[placa] if placa in self.__veiculos_cadastrados.keys() else None 

    def adiciona_veiculo(self, veiculo:Veiculo):
        if veiculo not in self.__veiculos_cadastrados and isinstance(veiculo, Veiculo):
            self.__veiculos_cadastrados[veiculo.placa] = veiculo

    def atualiza_veiculo(self, placa_atual, placa):
        self.__veiculos_cadastrados[placa] = self.__veiculos_cadastrados.pop(placa_atual)

    def atualiza_km_veiculo(self, veiculo:Veiculo, km):
        veiculo.atualiza_km(km)
        return veiculo.km

    def deleta_veiculo(self, placa):
        self.__veiculos_cadastrados.pop(placa)