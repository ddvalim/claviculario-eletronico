from PySimpleGUI import Window, Text, Button, Input, Column

from Validators.Funcionario import validator
from Abstracts.AbsctractTela import AbstractTela


class FiltraMovimentacao(AbstractTela):
    def __init__(self):
        self.window = Window('Filtro de negação').layout(
            [
                [Text('Deseja adicionar algum filtro?')],
                [Text('Motivo de negação'), Button('1')],
                [Text('Matrícula do funcionário'), Button('2')],
                [Text('Placa do carro'), Button('3')],
                [Text('Nenhum filtro'), Button('4')]
           ]
        )

class FiltraMotivoDeNegacao(AbstractTela):
    def __init__(self):
        self.window = Window('Filtro de Motivo de negação').layout(
            [
                [Text('Funcionário bloqueado'), Button('1')],
                [Text('Veiculo inválido'), Button('2')],
                [Text('Veiculo já retirado'), Button('3')],
                [Text('Veiculo já devolvido'), Button('4')],
                [Text('Funcionário não retirou e tentou devolver um Veiculo'), Button('5')],
           ]
        )


class Relatorio(AbstractTela):
    def __init__(self, movimentacoes):
        layout = [
        ]
        for mov in movimentacoes:
            movimentacao_layout = [
                [Text('*'*30)]
            ]
            if mov.veiculo is not None:
                movimentacao_layout.append([Text(f'Veiculo - {mov.veiculo.placa}')]) 
            switcher = {
                0: 'Retirada',
                1: 'Devolução'
            }
            movimentacao_layout += [
                [Text(f'Funcionario - {mov.funcionario.matricula} - {mov.funcionario.nome}')],
                [Text(f'Data - {str(mov.data)}')],
                [Text(f'Tipo - {switcher[mov.tipo]}')]
            ]
            motivo_negacao = {
                1: 'Funcionario bloqueado',
                2: 'Veiculo Inválido',
                3: 'Veiculo já retirado',
                4: 'Veiculo já devolvido',
                5: 'Funcionário não retirou e tentou devolver um Veiculo'
            }
            if mov.motivo_negacao is not None:
                movimentacao_layout.append([Text(f'Motivo Negacao - {motivo_negacao[mov.motivo_negacao]}')]) 

            layout += movimentacao_layout
        layout += [[Button('Voltar')]]
        self.window = Window('Movimentações').layout(
            [
                [Column(layout, scrollable=True)]
            ]
        )
class AcessosPorTipo(AbstractTela):
    def __init__(self):
        self.window = Window('Acessos por tipo').layout(
            [
                [Text('Infore um tipo de acesso:')],
                [Text('Acessos negados'), Button('1')],
                [Text('Acessos permitidos'), Button('2')],
                [Text('Todos os acessos'), Button('3')],
            ] 
        )