from Abstracts.abs_tela import AbstractTela

class TelaMovimentacoes(AbstractTela):
    def filtra_movimentacoes(self):
        print('*'*30)
        print('Deseja adicionar algum filtro?')
        print('1 - motivo de negação')
        print('2 - matrícula do funcionário')
        print('3 - placa do carro')
        print('Pressione enter se não deseja adicionar nenhum filtro')
        print('*'*30)
        try:
            val = input()
            if val == '':
                return None
            res = int(val)
        except Exception:
            self.excecao('Valor Inválido')
        dict_value = {
            1: self.filtra_motivo_de_negacao()
        }
        ret = None
        if res in dict_value.keys():
            ret = dict_value[res]
        else:
            ret = res
        return(ret)

    def filtra_motivo_de_negacao(self):
        invalid = True
        while invalid:
            print('1 - Funcionário bloqueado')
            print('2 - Veiculo inválido')
            print('3 - Veiculo já retirado')
            print('4 - Veiculo já devolvido')
            print('5 - Funcionário não retirou e tentou devolver um Veiculo')
            try:
                filtro = int(input())
            except ValueError:
                self.excecao('Valor inválido')
            if filtro in range(1,6):
                invalid = False        
        return { 1: filtro }
    

    def relatorio(self, movimentacoes):
        print('Movimentações:')

        for mov in movimentacoes:
            print('*'*30)
            print(f'Veiculo - {mov.veiculo.placa}') if mov.veiculo is not None else None
            print(f'Funcionario - {mov.funcionario.matricula} - {mov.funcionario.nome}')
            print(f'Data - {str(mov.data)}')
            switcher = {
                0: 'Retirada',
                1: 'Devolução'
            }
            print(f'Tipo - {switcher[mov.tipo]}')
            motivo_negacao = {
                1: 'Funcionario bloqueado',
                2: 'Veiculo Inválido',
                3: 'Veiculo já retirado',
                4: 'Veiculo já devolvido',
                5: 'Funcionário não retirou e tentou devolver um Veiculo'
            }
            print(f'Motivo Negacao - {motivo_negacao[mov.motivo_negacao]}') if mov.motivo_negacao is not None else None