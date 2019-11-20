import datetime

from .Telas import TelaListaFuncionarios, TelaAutenticacao, DetalhesDoFuncionario, AdicionaFuncionario, AtualizaFuncionario
from Abstracts.abs_tela import AbstractTela
from Validators.Funcionario import validator


class TelaFuncionarios(AbstractTela):
    def __init__(self):
        self.__validator = validator

    def adiciona_funcionario(self):
        func = {}
        for k in self.__validator.keys():
            invalid = True
            represent = k if k != 'data_nascimento' else 'data de nascimento no formato aaaa-mm-dd'
            while invalid:
                tela = AdicionaFuncionario(represent)
                _, _dict = tela.show()
                tela.close()
                inpu = _dict[represent]
                try:
                    inpu = self.__validator[k](
                        inpu) if self.__validator[k] != datetime.date else datetime.datetime.strptime(inpu, '%Y-%m-%d').date()
                except Exception:
                    self.excecao('Valor invalido para o campo')
                if isinstance(inpu, self.__validator[k]):
                    if self.__validator[k] == str:
                        if len(inpu) != 0:
                            invalid = False
                    elif self.__validator[k] == datetime.date:
                        if inpu < datetime.datetime.now().date():
                            invalid = False
                    else:
                        invalid = False
                    func[k] = inpu
        return func

    def autentica_funcionario(self):
        tela = TelaAutenticacao()
        botao, matricula = tela.show()
        matricula = matricula['matricula']
        tela.close()
        return matricula

    def funcionarios_cadastrados(self, funcs):
        tela = TelaListaFuncionarios(funcs)
        tela.show()
        tela.close()

    def atualiza_funcionario(self, funcionario):
        func = {}
        for k in self.__validator.keys():
            if k != 'matricula':
                invalid = True
                represent = k if k != 'data_nascimento' else 'data de nascimento no formato aaaa-mm-dd'
                while invalid:
                    tela = AtualizaFuncionario(represent, getattr(funcionario, k))
                    button, _dict = tela.show()
                    tela.close()
                    inpu = _dict[represent]
                    if button != 'Manter':
                        try:
                            inpu = self.__validator[k](
                                inpu) if self.__validator[k] != datetime.date else datetime.datetime.strptime(inpu, '%Y-%m-%d').date()
                        except Exception:
                            self.excecao('Valor invalido para o campo')
                        if isinstance(inpu, self.__validator[k]):
                            if self.__validator[k] == str:
                                if len(inpu) != 0:
                                    invalid = False
                            elif self.__validator[k] == datetime.date:
                                if inpu < datetime.datetime.now().date():
                                    invalid = False
                            else:
                                invalid = False
                            func[k] = inpu
                    else:
                        invalid = False
        return func

    def detalhes_do_funcionario(self, func):
       tela = DetalhesDoFuncionario(func)
       tela.show()
       tela.close()
