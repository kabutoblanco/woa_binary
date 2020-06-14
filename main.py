from problem.knapsack import Knapsack
from metaheuristics.simplestate.hillclimbing.hillclimbing_classic import HillclimbingClassic
from metaheuristics.simplestate.hillclimbing.hillclimbing_maxslope import HillclimbingMaxslope
from metaheuristics.simplestate.hillclimbing.random_search import RandomSearch
from metaheuristics.simplestate.vns.vns import VNS
from metaheuristics.population.woa_binary import WOABinary
from metaheuristics.population.woa_solution import WOASolution
from utils.statistics import Statistics
from data.export import Export

import copy
import math
import random
from time import time

def main():
    # w = WOABinary()
    # name_file = "./data/files/f2.txt"
    # k = Knapsack(name_file)
    # w = WOABinary(100)
    # w.max_efos = 1000
    # w.execute(k)
    # print(w.best_solution.fitness)
    # print(k.optimal_know)
    ITER_MAX = 30
    list_statistics = []
    e = Export(list_statistics)
    for i in range(1, 16):      
        name_file = ""
        if i < 11:
            name_file = "./data/files/f{}.txt".format(i)
        else:
            name_file = "./data/files/Knapsack{}.txt".format(i - 10)
        statistics = Statistics(name_file, i, ITER_MAX)
        k = Knapsack(name_file)
        hcc = HillclimbingClassic()
        hcm = RandomSearch()
        vns = VNS(0)
        woa = WOABinary(30)
        algorithms = []
        algorithms.append(woa)
        woa.max_efos = 5000
        information = [0] * 2
        sublist_statistics = [0] * len(algorithms)
        print(name_file)
        j = 0
        for algorithm in algorithms:
            vector = []
            successfull_count = 0
            start_time = time()          
            for l in range(ITER_MAX):
                random.seed(l)
                algorithm.execute(k, None)
                vector.append(algorithm.best_solution.fitness)
                successfull_count += 1 if algorithm.successfull else 0
            end_time = time()
            information[0] = algorithm.__str__()
            information[1] = vector
            statistics.set_vector(information)
            statistics.successfull_count = successfull_count
            sublist_statistics[j] = copy.deepcopy(statistics)
            print("{}min\t\t{}".format(round((end_time - start_time) / 60, 3), algorithm))
            j += 1
        list_statistics.append(copy.deepcopy(sublist_statistics)) 
    e.writeCSV()
    e.writeHTML()
    
if __name__ == "__main__":
    main()
