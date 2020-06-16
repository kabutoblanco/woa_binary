from .function import Function

import mpmath as mp

class Tanh(Function):
    def __init__(self):
        self.tao = 1

    def execute(self, A, Dist):
        return list(map(lambda x, y: (mp.exp(-self.tao * (x * y)) - 1) / (- self.tao * (x * y) + 1), A, Dist))

    # def execute(self, x_next):
    #     return list(map(lambda x: (mp.exp(-self.tao * x) - 1) / (- self.tao * x + 1), x_next))