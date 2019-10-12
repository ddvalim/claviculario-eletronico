class AbstractTela():
    def excecao(self, message):
        print('!'*30)
        print(f'Erro : {message}')
        print('!'*30)
        print('\n'*5)
        print('pressione enter para voltar ao menu')
        input()