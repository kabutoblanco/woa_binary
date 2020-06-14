from .variable import Variable
from data.file import File

class Knapsack:
    def __init__(self, file_name):
        self.total_items = 0
        self.capacity = 0.0
        self.optimal_know = 0.0
        self.variables = []
        self.load_data(file_name)

    def load_data(self, file_name):
        file = File(file_name)
        file.read()
        self.total_items = file.total_items
        self.capacity = file.capacity
        self.optimal_know = file.optimal_know
        i = 0
        for variable in file.items:
            v = Variable(i, variable[0], variable[1])
            self.variables.append(v)
            i += 1

    def evaluate(self, dimensions):        
        sum = [0] * 2
        i = 0
        for variable in self.variables:
            sum[0] += dimensions[i] * variable.value
            sum[1] += dimensions[i] * variable.weight
            i += 1
        return sum

    def get_weight(self, index):
        return self.variables[index].weight