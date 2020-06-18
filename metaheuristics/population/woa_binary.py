from ..algorithm import Algorithm, tm
from .woa_solution import WOASolution
from .transfer.sigma import Sigma
from .transfer.arctan import Arctan
from .transfer.tanh import Tanh

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
        self.transfer = Arctan()

    def init_whale(self, x):
        s = WOASolution(x, self)
        s.get_solution()
        return s
        
    def execute(self, obj_knapsack, value):
        self.reset_values()        
        self.AU = 2

        self.population_size = 30
        self.MAX_ITER = (self.max_efos - self.population_size) / (self.population_size + 8.7999999999)

        t = 0        
        factor_decre = 2 / self.MAX_ITER

        self.whales = list(map(lambda x: self.init_whale(obj_knapsack), range(self.population_size)))
        self.best_solution = max(self.whales, key = lambda x: x.fitness).copy()

        tm_s = tm()
        
        while self.efos < self.max_efos and t < self.MAX_ITER and not self.best_solution.is_optimalknow() and tm() - tm_s < self.max_time:
            for whale in self.whales:
                if self.efos >= self.max_efos or tm() - tm_s >= self.max_time:
                    break

                A = []
                C = []

                abs_A = 0

                for i in range(obj_knapsack.total_items):
                    au = random.uniform(-self.AU, self.AU)
                    Ai = 2 * au * random.random() - au
                    A.append(Ai)
                    C.append(2 * random.random())
                    if Ai >= 1:
                        abs_A = 1
                
                p = random.random()

                if p < 0.5:
                    if not abs_A:
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
                whale.tweak(0.61)   
                if whale.is_optimalknow():
                    self.best_solution = whale
                    break
                if self.efos >= self.max_efos or tm() - tm_s >= self.max_time:
                    break                        

            best_solution = max(self.whales, key = lambda x: x.fitness).copy()
            
            if best_solution.fitness > self.best_solution.fitness:
                self.best_solution = best_solution.copy()

            self.best_solution.local_optimizer()

            self.AU -= factor_decre
            t += 1  
            # print(self.AU)        

            if self.best_solution.is_optimalknow():
                break

        if self.best_solution.is_optimalknow():
            self.successfull = True        

    def __str__(self):
        return "BWOA " + self.transfer.__str__()