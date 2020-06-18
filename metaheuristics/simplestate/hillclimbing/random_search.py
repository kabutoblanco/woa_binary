from ...algorithm import Algorithm, tm
from ...solution import Solution
import copy
import random


class RandomSearch(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)

    def execute(self, obj_knapsack, obj_solution):
        self.reset_values()
        self.best_solution = Solution(obj_knapsack, self)
        self.best_solution.get_solution()

        tm_s = tm()

        while self.efos < self.max_efos and not self.best_solution.is_optimalknow() and tm() - tm_s < self.max_time:
            r = self.best_solution.copy()
            r.get_solution()

            if r.fitness > self.best_solution.fitness:
                self.best_solution = r

            if self.best_solution.is_optimalknow():
                self.successfull = True

    def __str__(self):
        return "Random Search"