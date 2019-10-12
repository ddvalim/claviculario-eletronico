import datetime
import re
from Veiculo.Veiculo import Veiculo
from Validators.Funcionario import validator

class Funcionario():
    def __init__(self, matricula, nome, data_nascimento, telefone, cargo):
        self.__validator = validator
        self.__validate_data(matricula=matricula, nome=nome, data_nascimento=data_nascimento, telefone=telefone, cargo=cargo)
        self.__matricula = matricula
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__telefone = telefone
        self.__cargo = cargo
        self.__veiculos_cadastrados = {}
    
    def __validate_data(self, *args, **kwargs):
        
        for k,v in kwargs.items():
            if not isinstance(v, self.__validator[k]):
                raise Exception(f'{k} is not instance of {self.__validator[k]}')
            if self.__validator[k] == str:
                if len(v) == 0:
                    raise Exception('String cannot be empty')
            if self.__validator[k] == datetime.date:
                if v > datetime.datetime.now().date() :
                    raise Exception('Date cannot be bigger than now') 

    @property
    def matricula(self):
        return self.__matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def telefone(self):
        return self.__telefone

    @property
    def cargo(self):
        return self.__cargo

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento =  data_nascimento

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    def adiciona_veiculo_cadastrado(self, veiculo):
        if isinstance(veiculo, Veiculo):
            self.__veiculos_cadastrados[veiculo.placa] = veiculo

    def adciona_veiculo_cadastrado(self, placa):
        del self.__veiculos_cadastrados[placa]
