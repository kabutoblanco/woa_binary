from .localsearch import Localsearch
from ....solution import Solution

import random
import copy

class LocalsearchBasic(Localsearch):
    
    def execute(self, obj_neighborhood):
        s = self.solution.copy()
        
        #  Selección aleatoria (S’) del vecindario actual (Nk) de S
        obj_neighborhood.execute(s)
        rand_index = random.randint(0, len(obj_neighborhood.neighborhood) - 1)
        
        s_prima = obj_neighborhood.neighborhood[rand_index]
        
        # Búsqueda local
        if s.obj_algorithm.max_efos - s.obj_algorithm.efos < self.algorithm.max_efos:
            self.algorithm.max_efos = s.obj_algorithm.max_efos - s.obj_algorithm.efos

        self.algorithm.ratio = obj_neighborhood.dh
        self.algorithm.pm = obj_neighborhood.pm
        s_prima.obj_algorithm = self.algorithm

        self.algorithm.execute(s.obj_knapsack, s_prima)
        s_prima2 = self.algorithm.best_solution
        s.obj_algorithm.efos += s_prima2.obj_algorithm.efos

        s_prima2.obj_algorithm = s.obj_algorithm

        return s_prima2
            

    