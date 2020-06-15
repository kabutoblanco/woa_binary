from abc import ABC, abstractclassmethod

class Algorithm(ABC):
    def __init__(self):
        self.efos = 0
        self.max_efos = 10
        self.successfull = False
        self.best_solution = None

    @abstractclassmethod
    def execute(self, obj_knapsack, obj_solution):
        raise NotImplementedError

    def reset_values(self):
        self.efos = 0
        self.successfull = False
        self.best_solution = None