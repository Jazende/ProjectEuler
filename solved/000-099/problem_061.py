import datetime
from operator import mul
from functools import reduce
from itertools import permutations

start = datetime.datetime.now()

class Figurate:
    def __init__(self):
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        return self.value()

    def __repr__(self):
        return f'{self.name}'

class Triangle(Figurate):
    name = 'tri'
    def value(self):
        return (self.start * (self.start + 1)) // 2

class Square(Figurate):
    name = 'squ'
    def value(self):
        return self.start * self.start

class Pentagonal(Figurate):
    name = 'pen'
    def value(self):
        return (self.start * ((3 * self.start) - 1)) // 2

class Hexagonal(Figurate):
    name = 'hex'
    def value(self):
        return self.start * ((2 * self.start) - 1)

class Heptagonal(Figurate):
    name = 'hep'
    def value(self):
        return (self.start * ((5 * self.start) - 3)) // 2

class Octagonal(Figurate):
    name = 'oct'
    def value(self):
        return self.start * ((3 * self.start) - 2)

class Number(int):
    def __init__(self, value):
        self.value = value

    def __call__(self):
        return self.value

    def __repr__(self):
        return f'{self.value}'

# Maak de Generators
tri, sqa, pen = Triangle(),  Square(),     Pentagonal()
hex, hep, oct = Hexagonal(), Heptagonal(), Octagonal()

# Lijst met de Figurate generators
figurates = [tri, sqa, pen, hex, hep, oct]

# dict voor alle 4 digit getallen voor elke figurate
four_digits = {figurate.name: [] for figurate in figurates}

# alle 4 digit getallen voor elke figurate
for figurate in figurates:
    while True:
        nr = next(figurate)
        if nr > 9999:
            break
        elif nr > 999:
            number = Number(nr)
            number.figurate = figurate.name
            number.sequence_number = figurate.start
            four_digits[figurate.name].append(number)

### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

def check_two_if_valid(number_one, number_two):
    if not (number_one % 100 == number_two // 100):
        return False
    if (number_one.sequence_number == number_two.sequence_number):
        return False
    return True

def resolve(perm, index, previous_number, first_number):
    if index == len(perm)-1:
        if not check_two_if_valid(previous_number, first_number):
            return 
        return first_number

    else:
        for next_number in four_digits[perm[index+1].name]:
            if not check_two_if_valid(previous_number, next_number):
                continue
            return resolve(perm, index+1, next_number, first_number)


perms = permutations(figurates, r=len(figurates))
sum_ = 0

for perm in perms:
    for first_number in four_digits[perm[0].name]:
        solution = resolve(perm, 0, first_number, first_number)
        if not solution is None:
            print(solution, end=" ")
            sum_ += solution

print(">", sum_)
