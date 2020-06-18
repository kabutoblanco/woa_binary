from ...algorithm import Algorithm, tm
from ...solution import Solution

import random

class HillclimbingMaxslope(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self.pm = 0.61
        self.ratio = 4
        self.neighborhood = 5

    def execute(self, obj_knapsack, obj_solution):
        self.reset_values()

        if not obj_solution:
            s = Solution(obj_knapsack, self)
            s.get_solution()
        else:
            s = obj_solution.copy()

        tm_s = tm()

        while self.efos < self.max_efos and not s.is_optimalknow() and tm() - tm_s < self.max_time:
            r = s.copy()
            r.tweak(self.pm, self.ratio)

            for v in range(self.neighborhood - 1):
                w = s.copy()
                w.tweak(self.pm, self.ratio)

                if w.fitness > r.fitness:
                    r = w
                if self.efos >= self.max_efos or s.is_optimalknow() or tm() - tm_s >= self.max_time:
                    break

            if r.fitness > s.fitness:
                s = r

            if s.fitness == obj_knapsack.optimal_know:
                self.successfull = True

        self.best_solution = s

    def __str__(self):
        return "Hillcliming MaxSlope"