from Validators.Funcionario import validator

class TelaFuncionarios():
    def __init__(self):
        self.__validator = validator
    def adiciona_funcionario(self):
        func = {}
        print('*' * 30)
        print('Adicionando funcionário...')
        print('*' * 30)
        for k in self.__validator.keys():
            represent = k if k != 'data_nascimento' else 'data de nascimento'
            print(f'Informe o/a {represent} do funcionário:')
            func[k] = input()
        return func