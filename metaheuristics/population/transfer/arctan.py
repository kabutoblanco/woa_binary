from .function import Function

import mpmath as mp

class Arctan(Function):
    def __init__(self):
        pass

    def execute(self, x_next):
        return list(map(lambda x: abs((2 / mp.math2.pi) * mp.math2.atan((mp.math2.pi / 2) * x)), x_next))

    def __str__(self):
        return "arctan"