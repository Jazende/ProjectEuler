import cProfile

def nr_solutions_above(target=1000):
    n = 0
    while True:
        count = 0
        max_x = n * 2 + 1
        for x in range(n+1, max_x):
            if (n*x) % (x-n) == 0:
                count += 1
            if count >= target*2:
                break
        if count >= target:
            break
        n += 1
    return n

# print(nr_solutions_above(1000))
cProfile.run('nr_solutions_above(1000)')

# def solutions_for_number(nr):
#     solutions = set()
#     max_x = nr * 2 + 1
#     for x in range(nr+1, max_x):
#         if (nr*x) % (x-nr) == 0:
#             y = (nr*x) / (x-nr)
#             y = int(y) if y.is_integer() else y
#             solutions.add((min(x, y), max(x, y)))
#     return sorted([x for x in solutions])

# def solutions_for_range(min_n, max_n):
#     solutions = {}

#     for n in range(min_n, max_n+1):
#         solutions[n] = set()
#         max_x = n * 2 + 1
#         for x in range(n+1, max_x):
#             if n*x % (x-n) == 0:
#                 y = (n*x) / (x-n)
#                 y = int(y) if y.is_integer() else y
#                 solutions[n].add((min(x, y), max(x, y)))
    
#     return solutions
