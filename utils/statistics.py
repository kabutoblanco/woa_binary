import numpy as np
import math

class Statistics:
    def __init__(self, name_file, seed, max_rep):
        self.name_file = name_file
        self.seed = seed
        self.a = np.array([])
        self.max_rep = max_rep

        self.algorithm = ""
        self.successfull_count = 0

    def set_vector(self, vector):
        self.algorithm = vector[0]
        self.a = np.array(vector[1])

    def average(self):
        return np.average(self.a)

    def std(self):
        return np.std(self.a)

    def successfull_rate(self):
        return self.successfull_count / self.max_rep * 100
    
    def total_average(self, statistics):
        total = len(statistics)        
        result = [0] * (3 * len(statistics[0]))
        for file in statistics:
            i = 0
            for algorithm in file:
                for j in range(3):
                    if j == 0:                    
                        result[i] += algorithm.average() / total
                    if j == 1:
                        result[i] += algorithm.std() / total
                    if j == 2:
                        result[i] += algorithm.successfull_rate() / total
                    i += 1
        return result
        
                
        
        
                
