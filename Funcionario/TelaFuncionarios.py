import datetime

from Abstracts.abs_tela import AbstractTela
from Validators.Funcionario import validator

class TelaFuncionarios(AbstractTela):
    def __init__(self):
        self.__validator = validator
    def adiciona_funcionario(self):
        func = {}
        print('*' * 30)
        print('Adicionando funcionário...')
        print('*' * 30)
        for k in self.__validator.keys():
            invalid = True
            represent = k if k != 'data_nascimento' else 'data de nascimento no formato aaaa-mm-dd'
            while invalid:    
                print(f'Informe o/a {represent} do funcionário:')
                inpu = input()
                try:
                    inpu = self.__validator[k](inpu) if self.__validator[k] != datetime.date else datetime.datetime.strptime(inpu, '%Y-%m-%d').date()
                except Exception:
                    print('valor invalido para o campo')
                if isinstance(inpu, self.__validator[k]):  
                    if self.__validator[k] == str:
                        if len(inpu) != 0:
                            invalid = False
                    elif self.__validator[k] == datetime.date:
                        if inpu < datetime.datetime.now().date() :
                            invalid = False 
                    else:
                        invalid = False
                    func[k] = inpu
        return func
