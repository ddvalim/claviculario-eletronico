from .Telas.telaExcecao import TelaExcecao

class AbstractTela():
    def excecao(self, message):
        tela = TelaExcecao(message)
        tela.show()
        tela.close()

    def sucesso(self, message):
        print('*'*30)
        print(f'Operação de {message} realizada com sucesso')
        print('*'*30)
        print('\n'*5)
        print('pressione enter para voltar ao menu')
        input()
    