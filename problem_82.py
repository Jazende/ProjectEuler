raw_input = """131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331"""


matrix = [[int(number) for number in line.split(",")]
          for line in raw_input.strip().split("\n")]

class Punt:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.n = None
        self.e = None
        self.w = None
        self.s = None

    def __repr__(self):
        return f"{self.x} - {self.y} - {self.value}"

weighted_matrix = [[Punt(idx_l, idx_r, int(number)) for idx_r, number in enumerate(line.split(","))]
                   for idx_l, line in enumerate(raw_input.strip().split("\n"))]

print(weighted_matrix)
