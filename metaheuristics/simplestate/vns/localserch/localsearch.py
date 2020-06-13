from abc import ABC

class Localsearch(ABC):

    def __init__(self, solution, algorithm):
        """Do the local search on vns base algorithm

        Parameters:
        solution (Solution): solution generator
        algorithm (Algorithm): Algorithm for local search

        Returns:
        none
        """
        self.solution = solution
        self.algorithm = algorithm
        self.efos = 0

    def execute(self, obj_neighborhood):
        raise NotImplementedError