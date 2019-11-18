from .Telas.telaExcecao import TelaExcecao
from .Telas.telaConfimarcao import telaConfirmacao
from .Telas.telaSucesso import telaSucesso

class AbstractTela():
    def excecao(self, message):
        tela = TelaExcecao(message)
        tela.show()
        tela.close()

    def sucesso(self, message):
        tela = telaSucesso(message)
        tela.show()
        tela.close()

    def confirmacao(self, acao):
        tela = telaConfirmacao(acao)
        resposta = tela.show()
        tela.close()
        return resposta
