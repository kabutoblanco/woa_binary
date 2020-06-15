from ...algorithm import Algorithm
from .neighborhood import Neighborhood
from ...solution import Solution
from ..hillclimbing.hillclimbing_classic import HillclimbingClassic
from ..hillclimbing.hillclimbing_maxslope import HillclimbingMaxslope
from .localserch.localsearch_basic import LocalsearchBasic
from .localserch.localsearch_desc import LocalsearchDesc
from .localserch.localsearch_redux import LocalsearchRedux

import math
import random

class VNS(Algorithm):
    def __init__(self, k_max):
        Algorithm.__init__(self)
        self.k_max = k_max
        self.neighborhoods = []

    def execute(self, obj_knapsack, obj_solution):
        self.reset_values()

        for i in range(0, self.k_max):
            neighborhood = Neighborhood(random.uniform(0.49, 0.61), i + 1, random.randint(4, 50))
            self.neighborhoods.append(neighborhood)

        s = Solution(obj_knapsack, self)
        s.get_solution()
        while self.efos < self.max_efos and s.fitness != obj_knapsack.optimal_know: 
            k = 0
            while k < self.k_max and self.efos < self.max_efos:
                obj_searchlocal = LocalsearchBasic(s, HillclimbingMaxslope())
                s_prima = obj_searchlocal.execute(self.neighborhoods[k])
                
                if s_prima.fitness > s.fitness:
                    s = s_prima
                    k = 0
                else:
                    k += 1

                if s.fitness == obj_knapsack.optimal_know:
                    self.successfull = True
                    break
            
        self.best_solution = s

    def __str__(self):
        return "VNS"
