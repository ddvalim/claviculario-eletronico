from abc import ABC, abstractmethod
from Exceptions.VoltarMenuException import VoltarMenuException

class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def show(self):
        button, value = self.window.Read()
        if button is None:
            raise VoltarMenuException()
        return button, value


    def close(self):
        self.window.Close()
