from .localsearch import Localsearch
from ....solution import Solution
import random
import copy

class LocalsearchDesc(Localsearch):
    
    def execute(self, obj_neighborhood):
        s = self.solution.copy()

        #  Selección aleatoria (S’) del vecindario actual (Nk) de S
        obj_neighborhood.execute(s)
        s_prima = obj_neighborhood.best_neighbors()
        
        return s_prima