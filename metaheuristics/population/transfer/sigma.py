from .function import Function

import mpmath as mp

class Sigma(Function):
    def __init__(self):
        pass

    def execute(self, A, Dist):
        return list(map(lambda x, y: 1 / (1 + mp.exp(-10 * (x * y - 0.5))), A, Dist))

    def execute(self, x_next):
        return list(map(lambda x: 1 / (1 + mp.exp(-10 * (x - 0.5))), x_next))