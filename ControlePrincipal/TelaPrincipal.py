from Abstracts.abs_tela import AbstractTela
from .Telas import MenuFuncionario, MenuMovimentacao, MenuVeiculo, MenuPrincipal


class TelaPrincipal(AbstractTela):
    def menu_principal(self):
        tela = MenuPrincipal()
        value, _ = tela.show()
        tela.close()
        return value

    def menu_funcionario(self):
        tela = MenuFuncionario()
        value, _ = tela.show()
        tela.close()
        return value

    def menu_veiculo(self):
        tela = MenuVeiculo()
        value, _ = tela.show()
        tela.close()
        return value

    def menu_movimentacao(self):
        tela = MenuMovimentacao()
        value, _ = tela.show()
        tela.close()
        return value
