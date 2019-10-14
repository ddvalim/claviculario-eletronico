class AbstractTela():
    def excecao(self, message):
        print('!'*30)
        print(f'Erro : {message}')
        print('!'*30)
        print('\n'*5)
        print('pressione enter para voltar ao menu')
        input()

    def sucesso(self, message):
        print('*'*30)
        print(f'Operação de {message} realizada com sucesso')
        print('*'*30)
        print('\n'*5)
        print('pressione enter para voltar ao menu')
        input()
    