from abc import ABC

class Algorithm(ABC):
    def __init__(self):
        self.efos = 0
        self.max_efos = 50
        self.successfull = False
        self.best_solution = None

    def execute(self, obj_knapsack, obj_solution):
        raise NotImplementedError