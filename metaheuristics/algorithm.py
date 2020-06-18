from abc import ABC, abstractclassmethod
from time import time as tm

class Algorithm(ABC):
    def __init__(self):
        self.efos = 0
        self.max_efos = 10
        self.successfull = False
        self.best_solution = None
        self.max_time = 0.5

    @abstractclassmethod
    def execute(self, obj_knapsack, obj_solution):
        raise NotImplementedError

    def reset_values(self):
        self.efos = 0
        self.successfull = False
        self.best_solution = None