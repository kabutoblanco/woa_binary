from .function import Function

import mpmath as mp

class Tanh(Function):
    def __init__(self):
        self.tao = 1

    def execute(self, x_next):
        return list(map(lambda x: (mp.exp(-self.tao * x) - 1) / (mp.exp(-self.tao * x) + 1), x_next))

    def __str__(self):
        return "tanh"