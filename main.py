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
    ITER_MAX = 30
    list_statistics = []
    e = Export(list_statistics)
    for i in range(1, 13):      
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
        algorithms.append(hcc)
        algorithms.append(hcm)
        algorithms.append(vns)
        algorithms.append(woa)
        hcc.max_efos = 5000
        hcm.max_efos = 5000
        vns.max_efos = 5000
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
                k_max = random.randint(2, int(math.log10(k.total_items) + 2)) if k.total_items < 6 else random.randint(3, int(math.log10(k.total_items) + 3))
                vns.k_max = k_max
                algorithm.execute(k, None)
                # print("[{}] - know: {}".format(algorithm.best_solution.fitness, k.optimal_know))
                vector.append(algorithm.best_solution.fitness)
                successfull_count += 1 if algorithm.successfull else 0
            end_time = time()
            information[0] = algorithm.__str__()
            information[1] = vector
            statistics.set_vector(information)
            statistics.successfull_count = successfull_count
            sublist_statistics[j] = copy.deepcopy(statistics)
            print("{}min\t{}".format(round((end_time - start_time) / 60, 3), algorithm))
            j += 1
        list_statistics.append(copy.deepcopy(sublist_statistics)) 
    e.writeCSV()
    e.writeHTML()
    
if __name__ == "__main__":
    main()
