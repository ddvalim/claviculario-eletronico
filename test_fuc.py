from Funcionario.Funcionario import Funcionario
import datetime

try:
    a = Funcionario(1,'abc', datetime.datetime(2019,1,1).date(),4,'a')
except Exception as ex:
    print(str(ex))