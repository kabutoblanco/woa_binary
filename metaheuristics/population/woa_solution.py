from ..solution import Solution

import copy
import mpmath as mp
import numpy as np
import random

class WOASolution(Solution):
    def __init__(self, obj_knapsack, obj_algorithm):
        super().__init__(obj_knapsack, obj_algorithm)

    def encircling_prey(self, best_solution, A, C):
        Yb = np.array(best_solution.dimensions)
        Yc = np.array(self.dimensions)
        A = np.array(A)
        C = np.array(C)
        # Dist = np.absolute(C * Yb - Yc)
        # c_step = self.sigma(A, Dist)
        # if random.random() < c_step:
        #     self.dimensions = list(map(lambda x: int(not x), self.dimensions))
        #     self.evaluate()
        Dist = np.absolute(C * Yb - Yc)
        c_step = np.absolute(self.tanh(A, Dist))
        self.dimensions = list(map(lambda x, y: 0 if random.random() < x else 1, c_step, self.dimensions))
        self.evaluate()

    def spiral_bubblenet_attacking(self, best_solution, A):
        Yb = np.array(best_solution.dimensions)
        Yc = np.array(self.dimensions)
        A = np.array(A)
        # Dist = Yb - Yc
        # c_step = self.sigma(A, Dist)
        # if random.random() < c_step:
        #     self.dimensions = list(map(lambda x: int(not x), self.dimensions))
        #     self.evaluate()
        Dist = Yb - Yc
        c_step = np.absolute(self.tanh(A, Dist))
        self.dimensions = list(map(lambda x, y: 0 if random.random() < x else 1, c_step, self.dimensions))
        self.evaluate()

    def prey_search(self, rand_solution, A, C):
        Yr = np.array(rand_solution.dimensions)
        Yc = np.array(self.dimensions)
        A = np.array(A)
        C = np.array(C)
        # Dist = np.absolute(C * Yr - Yc)
        # c_step = self.sigma(A, Dist)
        # if random.random() < c_step:
        #     self.dimensions = list(map(lambda x: int(not x), self.dimensions))
        #     self.evaluate()
        Dist = np.absolute(C * Yr - Yc)
        c_step = np.absolute(self.tanh(A, Dist))
        self.dimensions = list(map(lambda x, y: 0 if random.random() < x else 1, c_step, self.dimensions))
        self.evaluate()

    def sigma(self, A, Dist):
        # return 1 / (1 + mpmath.exp(-10 * (np.dot(A, Dist) - 0.5)))
        return list(map(lambda x, y: 1 / (1 + mp.exp(-10 * (x * y - 0.5))), A, Dist))
    
    def arctan(self, A, Dist):
        # return 1 / (1 + mpmath.exp(-10 * (np.dot(A, Dist) - 0.5)))
        return list(map(lambda x, y: (2 / mp.math2.pi) * mp.math2.atan((mp.math2.pi / 2) * (x * y)), A, Dist))

    def tanh(self, A, Dist):
        return list(map(lambda x, y: mp.math2.tanh(x * y), A, Dist))

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