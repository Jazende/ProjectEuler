# from functools import lru_cache

# @lru_cache(maxsize=None)
# def amount_by_size(grid_x, grid_y, block_x, block_y):
#     return max((grid_x - (block_x - 1)) * (grid_y - (block_y - 1)), 0)

# def squares_per_grid(grid_x, grid_y):
#     return sum(amount_by_size(grid_x, grid_y, x, y) for x in range(1, grid_x+1) for y in range(1, grid_y+1))

def easy_squares_per_grid(grid_x, grid_y):
    return sum(range(grid_x+1))*sum(range(grid_y+1))

target = 2_000_000
sum_of_numbers = [sum(range(1, x+1)) for x in range(2_001)]
set_of_solutions = []
base_index = 1
target_index = 1

while True:
    base = sum_of_numbers[base_index]
    target_index = 1
    while True:
        if (base * sum_of_numbers[target_index]) > target:
            break
        target_index += 1
    set_of_solutions.append((base, sum_of_numbers[target_index-1], base_index, target_index-1))
    set_of_solutions.append((base, sum_of_numbers[target_index], base_index, target_index))
    base_index += 1
    if base_index == len(sum_of_numbers):
        break

def difference(number):
    return abs(target-number)

def calc(input):
    return input[0] * input[1]

def area(input):
    return input[2] * input[3]

min_ = 2_000_000
result = None

for solution in set_of_solutions:
    new_sol = difference(calc(solution))
    if new_sol < min_:
        min_ = new_sol
        result = solution

print(min_, result, area(result))
# print(easy_squares_per_grid(36, 77))