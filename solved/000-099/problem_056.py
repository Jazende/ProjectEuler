def problem_56(target=100):
    "Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?"
    from itertools import product
    return max([sum([int(y) for y in str(x)]) for x in [x[0]**x[1] for x in list(product(range(1, target), range(1, target)))]])


problem_56()
