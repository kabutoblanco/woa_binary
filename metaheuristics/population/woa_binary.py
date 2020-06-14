from ..algorithm import Algorithm
from .woa_solution import WOASolution
import random
import numpy as np
import math

class WOABinary(Algorithm):
    def __init__(self, population_size):
        super().__init__()
        self.population_size = population_size
        self.whales = [None] * population_size

        self.MAX_ITEMS = 500
        self.AU = 2
        
    def execute(self, obj_knapsack, value):
        t = 0
        for i in range(self.population_size):
            s = WOASolution(obj_knapsack, self)
            s.get_solution()
            self.whales[i] = s
        self.whales.sort(key = lambda x: x.fitness, reverse = True)
        self.best_solution = self.whales[0]
        while self.efos < self.max_efos and t < self.MAX_ITEMS and self.best_solution.fitness != obj_knapsack.optimal_know:
            for whale in self.whales:
                au = [0] * obj_knapsack.total_items
                r1 = [0] * obj_knapsack.total_items
                r2 = [0] * obj_knapsack.total_items

                A = [0] * obj_knapsack.total_items
                C = [0] * obj_knapsack.total_items                
                for i in range(obj_knapsack.total_items):
                    au[i] = random.uniform(-self.AU, self.AU)
                    r1[i] = random.random()
                    r2[i] = random.random()

                for i in range(obj_knapsack.total_items):
                    A[i] = 2 * au[i] * r1[i] - au[i]
                    C[i] = 2 * r2[i]

                if random.random() < 0.5:
                    A_np = np.array(A)
                    A_normal = np.linalg.norm(A_np)
                    if A_normal < 1:
                        whale.encircling_prey(self.best_solution, A, C)
                    else:
                        index_rand = random.randint(0, self.population_size - 1)
                        whale_rand = self.whales[index_rand]
                        whale.prey_search(whale_rand, A, C)
                else:
                    whale.spiral_bubblenet_attacking(self.best_solution, A)
                whale.tweak(0.5)

            self.whales.sort(key = lambda x: x.fitness, reverse = True)
            if self.whales[0].fitness > self.best_solution.fitness:
                self.best_solution = self.whales[0].copy()

            self.AU -= 2 / (self.MAX_ITEMS + 1)
            t += 1        
        if self.best_solution.fitness == obj_knapsack.optimal_know:
            self.successfull = True

    def __str__(self):
        return "BWOA"