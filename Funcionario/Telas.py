from PySimpleGUI import Window, Text, Button, Input

from Validators.Funcionario import validator
from Abstracts.AbsctractTela import AbstractTela


class TelaAutenticacao(AbstractTela):
    def __init__(self):
        self.window = Window('Autenticação de Usuário').layout(
            [
                [Text('Informe sua matrícula: ')],
                [Input(key='matricula')],
                [Button('Ok!')]
            ]
        )


class TelaListaFuncionarios(AbstractTela):
    def __init__(self, funcs):
        self.window = Window('Funcionários')
        layout = [
            [Text('Funcionários:')],

        ]
        for func in funcs:
            layout.append([Text(f'{func.matricula} - {func.nome}')])
        layout.append([Button('Voltar')])
        self.window.layout(layout)

class DetalhesDoFuncionario(AbstractTela):
    def __init__(self, func):
        self.__validator = validator
        self.window = Window('Detalhes do funcionário')
        layout = [
            [Text('Funcionário:')],
        ]
        veics = []
        for veic in func.veiculos_cadastrados:
            veics.append([Text(f'     Placa: {veic.placa} -  Marca: {veic.marca} - Modelo: {veic.modelo} ')])
        fields_out_of_validator = [
            [Text((f'Bloqueado : {func.bloqueado}'))],
            [Text('Veiculos :')],
        ] + veics
        for k in self.__validator.keys():
            repres = k.title() if k != 'data_nascimento' else 'Data de nascimento'
            layout.append([Text(f'{repres} : {getattr(func, k)}')])
        layout += fields_out_of_validator
        layout.append([Button('Voltar')])
        self.window.layout(layout)

class AdicionaFuncionario(AbstractTela):
    def __init__(self, field):
        self.__validator = validator
        self.window = Window('Adiciona funcionário')
        layout = [
            [Text(f'Informe o/a {field} do funcionário:'), Input(key=field)],
            [Button('Ok!')]
        ]
        self.window.layout(layout)

class AtualizaFuncionario(AbstractTela):
    def __init__(self, field, value):
        self.__validator = validator
        self.window = Window('Atualiza funcionário')
        layout = [
            [Text(f'Informe o/a {field} do funcionário:'), Input(key=field, default_text=value)],
            [Button('Ok!'), Button('Manter')]
        ]
        self.window.layout(layout)
