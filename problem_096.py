import re
import time
import copy
import operator
import random


def func_called_timeout(old_func, count=20, time_out=1):
    old = old_func
    func_called_timeout_counter = 0
    def print(*args, **kwargs):
        nonlocal func_called_timeout_counter
        func_called_timeout_counter += 1 + sum([str(arg).count("\n") for arg in args])
        old(*args, **kwargs)
        if func_called_timeout_counter > count:
            time.sleep(time_out)
            func_called_timeout_counter = 0
    return print
# print = func_called_timeout(print, time_out=5)

re_sudoku = re.compile('Grid (\d{2})\s+(\d{9})\s+(\d{9})\s+(\d{9})\s+(\d{9})\s+(\d{9})\s+(\d{9})\s+(\d{9})\s+(\d{9})\s+(\d{9})')
set_of_nine = set(range(1, 10))

with open(r'problem_096_sudoku.txt', 'r') as f:
    raw_input = f.read()
raw_input = '''
Grid 01
800000000
003600000
070090200
050007000
000045700
000100030
001000068
008500010
090000400
'''

class SuDoKu(dict):
    def _valid_line(self, line_number):
        return len(set_of_nine) == len(self.get_line(line_number, type=set))

    def _valid_row(self, row_number):
        return len(set_of_nine) == len(self.get_row(row_number, type=set))

    def _valid_square(self, square_row, square_line):
        return set_of_nine == self.get_square(square_row//3, square_line//3, type=set)
        # return len(set_of_nine) == len(self.get_square(square_row//3, square_line//3, type=set))

    def is_valid(self):
        if not self._count_unfound() == 0:
            return False

        for x in range(3):
            for y in range(3):
                if not self._valid_square(x, y):
                    print('Invalid at square', x, y)
                    return False

        for x in range(9):
            if not self._valid_line(x):
                return False
            if not self._valid_row(x):
                return False

        return True

    def _count_unfound(self):
        return len([1 for value in self.values() if value == 0])

    def get_line(self, line_number, type):
        keys = ((x, line_number) for x in range(9))
        if type == 'keys':
            return list(keys)
        line = (self[key] for key in keys)
        if type == str:
            return "".join(str(cell) for cell in line)
        return type(line)

    def get_row(self, row_number, type):
        keys = ((row_number, x) for x in range(9))
        if type == 'keys':
            return list(keys)
        line = (self[key] for key in keys)
        if type == str:
            return "".join(str(cell) for cell in line)
        return type(line)

    def get_square(self, square_row, square_line, type):
        # keys = ((square_row*3+x, square_line*3+x) for x in range(3) for y in range(3))
        keys = set()
        for x in range(3):
            for y in range(3):
                keys.add(((square_row*3) + x, (square_line*3) + y))
        if type == 'keys':
            return keys
        line = (self[key] for key in keys)
        if type == str:
            return "".join(str(cell) for cell in line)
        return type(line)

    @classmethod
    def from_string(cls, _id, parts):
        new_sudoku = cls()
        new_sudoku._id = _id

        for y, line in enumerate(parts):
            for x, char in enumerate(line):
                new_sudoku[(x, y)] = int(char)
    
        return new_sudoku

    def __str__(self):
        return f'Sudoku {int(self._id)}:\n' + "\n".join(self.get_line(x, type=str) for x in range(9))

    def _cell_solutions(self, key):
        if self[key] > 0:
            return
        
        row_set = self.get_row(key[0], type=set)
        line_set = self.get_line(key[1], type=set)
        square_set = self.get_square(key[0]//3, key[1]//3, type=set)

        possible_answer = set_of_nine - line_set - row_set - square_set
        return possible_answer

    def solve(self):
        print(self)
        if self.is_valid():
            return True

        edits = 0

        # Check cells compared to outside
        for key, value in self.items():
            if not value == 0:
                continue

            cell_solutions = self._cell_solutions(key)

            if len(cell_solutions) == 0:
                return False
            if len(cell_solutions) == 1:
                self[key] = cell_solutions.pop()
                edits += 1

        # Check lines for where numbers can go
        for x in range(9):
            all_keys = set(key for key in self.keys() if key[1] == x)
            empty_keys = set(key for key in all_keys if self[key] == 0)
            numbers_to_find = set_of_nine - set(self[key] for key in all_keys)

            for number in numbers_to_find:
                possiblities = []
                for cell in empty_keys:
                    if number in self._cell_solutions(cell):
                        possiblities.append(cell)
                if len(possiblities) == 1:
                    self[possiblities[0]] = number
                    break

        # Check rows for where numbers can go
        for x in range(9):
            all_keys = set(key for key in self.keys() if key[0] == x)
            empty_keys = set(key for key in all_keys if self[key] == 0)
            numbers_to_find = set_of_nine - set(self[key] for key in all_keys)

            for number in numbers_to_find:
                possiblities = []
                for cell in empty_keys:
                    if number in self._cell_solutions(cell):
                        possiblities.append(cell)
                if len(possiblities) == 1:
                    self[possiblities[0]] = number
                    break

        # Check squares for where numbers can go:
        for x in range(3):
            for y in range(3):
                all_keys = set(key for key in self.keys() if key[0]//3 == x and key[1]//3 == y)
                empty_keys = set(key for key in all_keys if self[key] == 0)
                numbers_to_find = set_of_nine - set(self[key] for key in all_keys)

                for number in numbers_to_find:
                    possiblities = []
                    for cell in empty_keys:
                        if number in self._cell_solutions(cell):
                            possiblities.append(cell)
                    if len(possiblities) == 1:
                        self[possiblities[0]] = number
                        break
    
        if edits > 0:
            return self.solve()

        return False

    def iterative_solve_attempt(self):
        self.solve()

        empty_keys = [key for key, value in self.items() if value == 0]
        
        solutions = {}

        for key in empty_keys:
            poss_solutions = self._cell_solutions(key)
            solutions[key] = []

            for solution in poss_solutions:
                copied = copy.deepcopy(self)
                copied[key] = solution
                copied.solve()
                if copied.is_valid():
                    solutions[key].append(solution)

        edits = 0
        for key, value in solutions.items():
            if not len(value) == 1:
                continue
            self[key] = value[0]
            edits += 1
        
        if edits > 1:
            self.solve()

    def get_top_left_three(self):
        return (self[(0, 0)] * 100) + (self[(1, 0)] * 10) + self[(2, 0)]

def problem_96(raw_input):
    raw_grids = re_sudoku.findall(raw_input)
    grids = [SuDoKu.from_string(gr[0], gr[1:]) for gr in raw_grids]

    for grid in grids:
        grid.iterative_solve_attempt()

    print(sum([g.get_top_left_three() for g in grids]))
    return sum([g.get_top_left_three() for g in grids])


problem_96(raw_input)
