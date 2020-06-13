class Neighborhood:
    def __init__(self, pm, dh, size):
        self.pm = pm
        self.dh = dh
        self.size = size
        self.neighborhood = []

    def execute(self, s):
        i = 0
        while i < self.size and s.obj_algorithm.efos < s.obj_algorithm.max_efos:
            r = s.copy()
            r.tweak(self.pm, self.dh)
            self.neighborhood.append(r)
            i += 1            

    def best_neighbors(self):
        best = self.neighborhood[0]

        for neighbor in self.neighborhood:
            if neighbor.fitness > best.fitness:
                best = neighbor.copy()
        
        return best

    def __str__(self):
        return str(self.dh)