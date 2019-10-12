from Exceptions.entradaInvalidaException import EntradaInvalidaException


class Veiculo:

    def __init__(self, placa: str, modelo: str, marca: str, ano: int, km: int):
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__km = km

    # GETTERS & SETTERS

    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self, placa):
        self.__placa = placa
    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    @property
    def km(self):
        return self.__km
    @km.setter
    def km(self, km):
        self.__km = km

    # METODOS

    def atualiza_km(self, km_andados):
        if isinstance(km_andados, str):
            raise EntradaInvalidaException()
        self.__km += km_andados
        return "Quilometragem atualizada -  Total de quilometros andados: " + str(self.__km)