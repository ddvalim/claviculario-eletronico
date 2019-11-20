from abc import ABC, abstractmethod


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def show(self):
        return self.window.Read()


    def close(self):
        self.window.Close()
