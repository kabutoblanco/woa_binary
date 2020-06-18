from abc import ABC, abstractclassmethod

class Function(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def execute(self, x_next):
        raise NotImplementedError
