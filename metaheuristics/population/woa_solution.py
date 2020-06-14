from ..solution import Solution

import copy
import math
import numpy as np
import random

class WOASolution(Solution):
    def __init__(self, obj_knapsack, obj_algorithm):
        super().__init__(obj_knapsack, obj_algorithm)

    def encircling_prey(self, best_solution, A, C):
        A = np.array(A)
        C = np.array(C)
        Yb = np.array(best_solution.dimensions)
        Yc = np.array(self.dimensions)
        Dist = np.absolute((C * Yb) - Yc)
        c_step = 1 / (1 + np.exp(-10 * (np.dot(A, Dist) - 0.5)))
        if random.random() < c_step:
            for i in range(len(self.dimensions)):
                self.dimensions[i] = int(not self.dimensions[i])
            self.evaluate()

    def spiral_bubblenet_attacking(self, best_solution, A):
        A = np.array(A)
        Yb = np.array(best_solution.dimensions)
        Yc = np.array(self.dimensions)
        Dist = Yb - Yc
        c_step = 1 / (1 + np.exp(-10 * (np.dot(A, Dist) - 0.5)))       
        if random.random() < c_step:
            for i in range(len(self.dimensions)):
                self.dimensions[i] = int(not self.dimensions[i])
            self.evaluate()

    def prey_search(self, rand_solution, A, C):
        A = np.array(A)
        C = np.array(C)
        Yb = np.array(rand_solution.dimensions)
        Yc = np.array(self.dimensions)
        Dist = np.absolute((C * Yb) - Yc)
        c_step = 1 / (1 + np.exp(-10 * (np.dot(A, Dist) - 0.5)))        
        if random.random() < c_step:
            for i in range(len(self.dimensions)):
                self.dimensions[i] = int(not self.dimensions[i])
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