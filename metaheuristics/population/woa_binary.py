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
        self.MAX_ITER = 0
        self.AU = 0
        
    def execute(self, obj_knapsack, value):
        self.reset_values()
        self.MAX_ITER = 500
        self.AU = 2
        t = 0        
        factor_decre = 2 / self.MAX_ITER
        for i in range(self.population_size):
            s = WOASolution(obj_knapsack, self)
            s.get_solution()
            self.whales[i] = s
        self.whales.sort(key = lambda x: x.fitness, reverse = True)
        self.best_solution = self.whales[0]
        while self.efos < self.max_efos and t < self.MAX_ITER and self.best_solution.fitness != obj_knapsack.optimal_know:
            for whale in self.whales:
                if self.efos > self.max_efos:
                    break
                au = [0] * obj_knapsack.total_items
                r1 = [0] * obj_knapsack.total_items
                r2 = [0] * obj_knapsack.total_items

                A = [0] * obj_knapsack.total_items
                C = [0] * obj_knapsack.total_items

                au = list(map(lambda x: random.uniform(-self.AU, self.AU), au))
                r1 = list(map(lambda x: random.random(), r1))
                r2 = list(map(lambda x: random.random(), r2))

                A = list(map(lambda x, y: 2 * x * y - x, au, r1))
                C = list(map(lambda x: 2 * x, r2))

                if random.random() < 0.5:
                    A_np = np.array(A)
                    A_module = np.linalg.norm(A_np)
                    if A_module < 1:
                        # print("Asechando presa")
                        whale.encircling_prey(self.best_solution, A, C)
                    else:
                        # print("Buscando presa")
                        index_rand = random.randint(0, self.population_size - 1)
                        whale_rand = self.whales[index_rand]
                        whale.prey_search(whale_rand, A, C)
                else:
                    # print("Atacando presa")
                    whale.spiral_bubblenet_attacking(self.best_solution, A)                    
                if whale.weight > whale.obj_knapsack.capacity:
                    whale.tweak(0.75)                

            self.whales.sort(key = lambda x: x.fitness, reverse = True)
            
            if self.whales[0].fitness > self.best_solution.fitness:
                self.best_solution = self.whales[0].copy()

            self.AU -= factor_decre
            t += 1                          

        if self.best_solution.fitness == obj_knapsack.optimal_know:
            self.successfull = True        

    def __str__(self):
        return "BWOA"