from ..solution import Solution
from ..simplestate.hillclimbing.hillclimbing_classic import HillclimbingClassic

import copy
import mpmath as mp
import numpy as np
import random

class WOASolution(Solution):
    def __init__(self, obj_knapsack, obj_algorithm):
        super().__init__(obj_knapsack, obj_algorithm)
        self.transfer = obj_algorithm.transfer
        self.b = 1

    def encircling_prey(self, best_solution, A, C):
        self.weight = 0
        Yb = np.array(best_solution.dimensions)
        Yc = np.array(self.dimensions)
        A = np.array(A)
        C = np.array(C)
        Dist = np.absolute(C * Yb - Yc)
        x_next = Yb - A * Dist
        c_step = self.transfer.execute(x_next)
        # Dist = np.absolute(C * Yb - Yc)
        # c_step = self.transfer.execute(A * Dist)
        # print("rodeando: {}".format(c_step))
        self.dimensions = list(map(lambda x, y: 1 if random.random() < x else 0, c_step, Yc))
        self.weight = sum(self.dimensions[i] * self.obj_knapsack.get_weight(i) for i in range(len(self.dimensions)))

    def spiral_bubblenet_attacking(self, best_solution, A):
        self.weight = 0
        Yb = np.array(best_solution.dimensions)
        Yc = np.array(self.dimensions)
        A = np.array(A) 
        Dist = np.absolute(Yb - Yc)
        l = random.uniform(-1, 1)
        x_next = Dist * mp.exp(self.b * l) * mp.cos(2 * mp.pi * l) + Yb
        c_step = self.transfer.execute(x_next)
        # Dist = Yb - Yc
        # c_step = self.transfer.execute(A * Dist)
        # print("atacando: {}".format(c_step))
        self.dimensions = list(map(lambda x, y: 1 if random.random() < x else 0, c_step, Yc))
        self.weight = sum(self.dimensions[i] * self.obj_knapsack.get_weight(i) for i in range(len(self.dimensions)))
        # self.evaluate()

    def prey_search(self, rand_solution, A, C):
        self.weight = 0
        Yr = np.array(rand_solution.dimensions)
        Yc = np.array(self.dimensions)
        A = np.array(A)
        C = np.array(C)
        Dist = np.absolute(C * Yr - Yc)
        x_next = Yr - A * Dist
        c_step = self.transfer.execute(x_next)       
        # Dist = np.absolute(C * Yr - Yc)
        # c_step = self.transfer.execute(A * Dist)
        # print("buscando: {}".format(c_step))
        self.dimensions = list(map(lambda x, y: 1 if random.random() < x else 0, c_step, Yc))
        self.weight = sum(self.dimensions[i] * self.obj_knapsack.get_weight(i) for i in range(len(self.dimensions)))
        # self.evaluate()

    def local_optimizer(self):
        count = 0        
        while count < 10:
            copy = self.copy()
            dh = 4
            copy.tweak_origin(0.61, dh)
            if copy.fitness > self.fitness:
                self.dimensions = copy.dimensions
                self.fitness = copy.fitness
                self.weight = copy.weight
            count += 1

    def tweak_origin(self, pm, dh):
        super().tweak(pm, dh)
    
    def tweak(self, pm):
        checks = []
        while self.weight > self.obj_knapsack.capacity:
            if random.random() < pm:
                index = random.randint(0, len(self.dimensions) - 1)
                if index not in checks and self.dimensions[index] == 1:
                    checks.append(index)
                    self.dimensions[index] = 0
                    self.weight -= self.obj_knapsack.get_weight(index)
        
        checks = []
        dimensions = copy.copy(self.dimensions)
        while True:
            if random.random() < pm:
                index = random.randint(0, len(self.dimensions) - 1)
                if index not in checks and self.dimensions[index] == 0:
                    checks.append(index)
                    dimensions[index] = 1
                    self.dimensions[index] = 1
                    self.weight += self.obj_knapsack.get_weight(index)
                    weight = copy.copy(self.weight)
                    if self.weight > self.obj_knapsack.capacity:
                        self.dimensions[index] = 0
                        self.weight -= self.obj_knapsack.get_weight(index)
                        checks.remove(index)
                    if weight == self.obj_knapsack.capacity:
                        break
                    if weight > self.obj_knapsack.capacity and 0 not in dimensions:
                        break                    

        self.evaluate()       
    
    def __str__(self):
        return super().__str__()