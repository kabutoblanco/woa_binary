from .function import Function

import mpmath as mp

class Arctan(Function):
    def __init__(self):
        pass

    def execute(self, A, Dist):
        return list(map(lambda x, y: (2 / mp.math2.pi) * mp.math2.atan((mp.math2.pi / 2) * (x * y)), A, Dist))