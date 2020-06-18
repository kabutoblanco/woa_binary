from .function import Function

import mpmath as mp

class Sigma(Function):
    def __init__(self):
        pass

    def execute(self, x_next):
        return list(map(lambda x: 1 / (1 + mp.exp(-x / 3)), x_next))

    def __str__(self):
        return "sigma"