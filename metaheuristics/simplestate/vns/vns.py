from ...algorithm import Algorithm, tm
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
        self.k_max = random.randint(2, int(math.log10(obj_knapsack.total_items) + 2)) if obj_knapsack.total_items < 6 else random.randint(3, int(math.log10(obj_knapsack.total_items) + 3))

        for i in range(0, self.k_max):
            neighborhood = Neighborhood(random.uniform(0.49, 0.61), i + 1, random.randint(4, 50))
            self.neighborhoods.append(neighborhood)

        s = Solution(obj_knapsack, self)
        s.get_solution()

        tm_s = tm()

        while self.efos < self.max_efos and not s.is_optimalknow() and tm() - tm_s < self.max_time: 
            k = 0
            while k < self.k_max and self.efos < self.max_efos and tm() - tm_s < self.max_time:
                obj_searchlocal = LocalsearchBasic(s, HillclimbingMaxslope())
                s_prima = obj_searchlocal.execute(self.neighborhoods[k])
                
                if s_prima.fitness > s.fitness:
                    s = s_prima
                    k = 0
                else:
                    k += 1

                if s.is_optimalknow():
                    self.successfull = True
                    break
            
        self.best_solution = s

    def __str__(self):
        return "VNS"
