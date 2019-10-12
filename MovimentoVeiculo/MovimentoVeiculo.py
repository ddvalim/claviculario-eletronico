import datetime

class MovimentoVeiculo():
    def __init__(self, veiculo, funcionario, tipo, motivoNegacao=None):
        self.__veiculo = veiculo
        self.__funcionario = funcionario
        self.__data = datetime.datetime.now()
        self.__tipo = tipo
        self.__motivo_negacao = motivoNegacao

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def tipo(self):
        return self.__tipo

    @property
    def data(self):
        return self.__data

    @property
    def motivo_negacao(self):
        return self.__motivo_negacao
