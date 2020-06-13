from .localsearch import Localsearch
from ....solution import Solution
import random
import copy

class LocalsearchRedux(Localsearch):

    def execute(self, obj_neighborhood):
        s = self.solution.copy()

        #  Selección aleatoria (S’) del vecindario actual (Nk) de S
        obj_neighborhood.execute(s)
        rand_index = random.randint(0, len(obj_neighborhood.neighborhood) - 1)
        s_prima = obj_neighborhood.neighborhood[rand_index]

        return s_prima