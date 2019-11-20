from Abstracts.abs_tela import AbstractTela
from .Telas import FiltraMovimentacao, FiltraMotivoDeNegacao, Relatorio, AcessosPorTipo

class TelaMovimentacoes(AbstractTela):
    def filtra_movimentacoes(self):
        tela= FiltraMovimentacao()
        val, _ = tela.show()
        tela.close()
        if val == '4':
            return None
        res = int(val)
        dict_value = {
            1: self.filtra_motivo_de_negacao
        }
        ret = None
        if res in dict_value.keys():
            ret = dict_value[res]()
        else:
            ret = res
        return ret

    def filtra_motivo_de_negacao(self):
        tela = FiltraMotivoDeNegacao()
        value, _ = tela.show()
        tela.close() 
        return { 1: int(value) }
    
    def acessos_por_tipo(self):
        tela = AcessosPorTipo()
        value, _ = tela.show()
        tela.close()
        return value
        

    def relatorio(self, movimentacoes):
        tela = Relatorio(movimentacoes)
        tela.show()
        tela.close()