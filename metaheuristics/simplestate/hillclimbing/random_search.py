from ..algorithm import Algorithm
from ...solution import Solution
import copy
import random


class RandomSearch(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)

    def execute(self, obj_knapsack, obj_solution):
        self.efos = 0
        self.best_solution = Solution(obj_knapsack, self)
        self.best_solution.get_solution()

        while self.efos < self.max_efos and self.best_solution.fitness != obj_knapsack.optimal_know:
            r = self.best_solution.copy()
            r.get_solution()

            if r.fitness > self.best_solution.fitness:
                self.best_solution = r

            if self.best_solution.fitness == obj_knapsack.optimal_know:
                self.successfull = True

    def __str__(self):
        return "Random Search"