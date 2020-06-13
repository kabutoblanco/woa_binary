import copy
import random

class Solution:
    
    def __init__(self, obj_knapsack, obj_algorithm):
        self.fitness = 0
        self.obj_knapsack = obj_knapsack
        self.obj_algorithm = obj_algorithm
        self.dimensions = [0] * obj_knapsack.total_items
        self.weight = 0
    
    def copy(self):
        clone = copy.copy(self)
        clone.dimensions = copy.copy(self.dimensions)
        return clone

    def get_solution(self):
        self.dimensions = [0] * self.obj_knapsack.total_items
        self.weight = 0

        weight = 0
        checks = []

        while len(checks) < self.obj_knapsack.total_items:
            if random.random() < 0.61:
                index = random.randint(0, len(self.dimensions) - 1)
                if index not in checks:
                    self.dimensions[index] = random.randint(0, 1)
                    checks.append(index)
                    if self.dimensions[index] == 1:             
                        weight += self.obj_knapsack.get_weight(index)
                        if weight > self.obj_knapsack.capacity:
                            self.dimensions[index] = 0
                            break
                        self.weight += self.obj_knapsack.get_weight(index)

        self.evaluate()

    def tweak(self, pm, dh):
        checks = []
        dimensions = copy.copy(self.dimensions)

        while len(checks) < dh:
            if random.random() < pm:
                index = random.randint(0, len(self.dimensions) - 1)
                if index not in checks:
                    self.dimensions[index] = int(not self.dimensions[index])
                    checks.append(index)
                    if self.dimensions[index] == 1:
                        self.weight += self.obj_knapsack.get_weight(index)
                        weight = copy.copy(self.weight)
                        if self.weight > self.obj_knapsack.capacity:
                            self.dimensions[index] = 0
                            self.weight -= self.obj_knapsack.get_weight(index)                            
                            checks.remove(index)
                        if weight == self.obj_knapsack.capacity:
                            break
                        if weight > self.obj_knapsack.capacity and 1 not in dimensions:
                            break                        
                    else:
                        self.weight -= self.obj_knapsack.get_weight(index)
                        dimensions[index] = 0

        self.evaluate()

    def evaluate(self):
        self.fitness = self.obj_knapsack.evaluate(self.dimensions)
        self.obj_algorithm.efos += 1

    def __str__(self):
        return self.dimensions.__str__()
