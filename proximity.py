from math import sqrt


class ProximityMeasure:
    def __init__(self, row1, row2):
        self.row1 = row1
        self.row2 = row2

    def hamming(self):
        return sum(abs(x1 - x2) for x1, x2 in zip(self.row1, self.row2)) / len(self.row1)

    def euclidean(self):
        return sqrt(sum((x1 - x2) ** 2 for x1, x2 in zip(self.row1, self.row2)))

    def manhattan(self):
        return sum(abs(x1-x2) for x1, x2 in zip(self.row1, self.row2))

    def minkowski(self, order):
        return sum(abs(x1-x2)**order for x1, x2 in zip(self.row1, self.row2))**(1/order)
