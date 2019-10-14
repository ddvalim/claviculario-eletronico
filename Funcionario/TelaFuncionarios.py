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

    def autentica_funcionario(self):
        print('*' * 30)
        print('Informe a matrícula do usuário')
        return input()
    
    def funcionarios_cadastrados(self, funcs):
        print('*'*30)
        print('Funcionários:')
        for func in funcs:
            print(f'> {func.matricula} - {func.nome}')
        print('Pressione enter para continuar')
        return input()
    
    def atualiza_funcionario(self, funcionario):
        func = {}
        print('*' * 30)
        print('Atualizando funcionário...')
        print('*' * 30)
        for k in self.__validator.keys():
            if k != 'matricula':
                invalid = True
                represent = k if k != 'data_nascimento' else 'data de nascimento no formato aaaa-mm-dd'
                while invalid:    
                    print(f'{represent} do funcionário : {getattr(funcionario, k)}')
                    print(f'Informe o/a {represent} do funcionário (aperte enter se não deseja mudar):')
                    inpu = input()
                    if inpu != '':
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
                    else:
                        invalid = False
        return func
    
    def deleta_funcionario(self, funcionario):
        print('*'*30)
        print(f'Tem certeza que deseja deletar o funcionário -> {funcionario.nome}?')
        print('s - sim, n - nao')
        return True if input().lower() == 's' else False

    def detalhes_do_funcionario(self, func):
        print('*'*30)
        print('Funcionário: ')
        for k in self.__validator.keys():
            repres = k.title() if k != 'data_nascimento' else 'Data de nascimento'
            print(f'{repres} : {getattr(func, k)}')
        print(f'Bloqueado : {func.bloqueado}')
        print('Veiculos cadastrados:')
        for veic in func.veiculos_cadastrados:
            print(f'placa: {veic.placa} -  marca: {veic.marca} - modelo: {veic.modelo} ')
        print('*'*30)
        print('Pressione enter para continuar')
        input()
