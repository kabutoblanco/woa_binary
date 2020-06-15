from ..solution import Solution
from .transfer.sigma import Sigma
from .transfer.arctan import Arctan
from .transfer.tanh import Tanh

import copy
import mpmath as mp
import numpy as np
import random

class WOASolution(Solution):
    def __init__(self, obj_knapsack, obj_algorithm):
        super().__init__(obj_knapsack, obj_algorithm)
        self.tranfer = Sigma()
        self.b = 1

    def encircling_prey(self, best_solution, A, C):
        Yb = np.array(best_solution.dimensions)
        Yc = np.array(self.dimensions)
        A = np.array(A)
        C = np.array(C)
        # Dist = np.absolute(C * Yb - Yc)
        # x_next = Yb - A * Dist
        # c_step = np.absolute(self.tranfer.execute(x_next))
        Dist = np.absolute(C * Yb - Yc)
        c_step = np.absolute(self.tranfer.execute(A, Dist))
        self.dimensions = list(map(lambda x, y: int(not y) if random.random() < x else y, c_step, self.dimensions))
        self.evaluate()

    def spiral_bubblenet_attacking(self, best_solution, A):
        Yb = np.array(best_solution.dimensions)
        Yc = np.array(self.dimensions)
        A = np.array(A)
        # Dist = np.absolute(Yb - Yc)
        # l = random.uniform(-1, 1)
        # x_next = Dist * mp.exp(self.b * l) * mp.cos(2 * mp.pi * l) + Yc
        # c_step = np.absolute(self.tranfer.execute(x_next))
        Dist = Yb - Yc
        c_step = np.absolute(self.tranfer.execute(A, Dist))
        self.dimensions = list(map(lambda x, y: int(not y) if random.random() < x else y, c_step, self.dimensions))
        self.evaluate()

    def prey_search(self, rand_solution, A, C):
        Yr = np.array(rand_solution.dimensions)
        Yc = np.array(self.dimensions)
        A = np.array(A)
        C = np.array(C)
        # Dist = np.absolute(C * Yr - Yc)
        # x_next = Yr - A * Dist
        # c_step = np.absolute(self.tranfer.execute(x_next))
        Dist = np.absolute(C * Yr - Yc)
        c_step = np.absolute(self.tranfer.execute(A, Dist))
        self.dimensions = list(map(lambda x, y: int(not y) if random.random() < x else y, c_step, self.dimensions))
        self.evaluate()

    def tweak(self, pm):
        checks = []
        while self.weight > self.obj_knapsack.capacity:
            if random.random() < pm:
                index = random.randint(0, len(self.dimensions) - 1)
                if index not in checks and self.dimensions[index] == 1:
                    checks.append(index)
                    self.dimensions[index] = int(not self.dimensions[index])
                    self.weight -= self.obj_knapsack.get_weight(index)
        
        checks = []
        while self.weight < self.obj_knapsack.capacity:
            if random.random() < pm:
                index = random.randint(0, len(self.dimensions) - 1)
                if index not in checks and self.dimensions[index] == 0:
                    checks.append(index)
                    self.dimensions[index] = int(not self.dimensions[index])
                    self.weight += self.obj_knapsack.get_weight(index)
                    if self.weight == self.obj_knapsack.capacity:
                        break
                    if self.weight > self.obj_knapsack.capacity:
                        self.dimensions[index] = 0
                        self.weight -= self.obj_knapsack.get_weight(index)
                        break

        self.evaluate()       
    
    def __str__(self):
        return super().__str__()