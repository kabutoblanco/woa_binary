class Variable:
    def __init__(self, position, value, weight):
        self.position = position
        self.value = value
        self.weight = weight
        self.density = self.value / self.weight

    def __str__(self):
        return "pos: {} - value: {} - weight: {}".format(self.position, self.value, self.weight)