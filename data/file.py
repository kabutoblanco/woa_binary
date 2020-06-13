class File:
    def __init__(self, file_name):
        self.fn = file_name
        self.total_items = 0
        self.capacity = 0
        self.items = []
        self.optimal_know = 0

    def read(self):
        with open(self.fn, "r") as archivo:
            first_line = archivo.readline().split(" ")
            self.total_items = int(first_line[0])
            self.capacity = int(first_line[1])
            for i in range(0, self.total_items):
                sp = archivo.readline().replace(',', '.').split(" ")
                self.items.append([float(sp[0]), float(sp[1])])
            self.optimal_know = float(archivo.readline().replace(',', '.'))
            opt = archivo.readline().split(" ")
