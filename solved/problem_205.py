from itertools import product

peter = product([1, 2, 3, 4], repeat=9)

p_count = 0
p_values = {x: 0 for x in range(1*9, 4*9+1)}
while True:
    try:
        next_ = next(peter)
    except StopIteration:
        break
    p_values[sum(next_)] += 1
    p_count += 1

colin  = product([1, 2, 3, 4, 5, 6], repeat=6)

c_count = 0
c_values = {x: 0 for x in range(1*6, 6*6+1)}
while True:
    try:
        next_ = next(colin)
    except StopIteration:
        break
    c_values[sum(next_)] += 1
    c_count += 1

# % appearance of p_value (p_value / p_count) * sum % appearence c_value < p_value 
chance = sum([(p_values[x] / p_count) * (sum([c_values[y] for y in c_values.keys() if y < x]) / c_count) for x in p_values.keys()])
print(round(chance, 7))



# from itertools import product

# peter = product([1, 2, 3, 4], repeat=9)

# p_count = 0
# p_values = {x: 0 for x in range(1*9, 4*9+1)}
# while True:
#     try:
#         next_ = next(peter)
#     except StopIteration:
#         break
#     p_values[sum(next_)] += 1
#     p_count += 1

# colin  = product([1, 2, 3, 4, 5, 6], repeat=6)

# c_count = 0
# c_values = {x: 0 for x in range(1*6, 6*6+1)}
# while True:
#     try:
#         next_ = next(colin)
#     except StopIteration:
#         break
#     c_values[sum(next_)] += 1
#     c_count += 1

# peter_chances = {x: (p_values[x] / p_count, sum([c_values[y] for y in c_values.keys() if y < x]) / c_count) for x in p_values.keys()}

# chance = sum([v[0] * v[1] for k, v in peter_chances.items()])
# print(round(chance, 7))