def problem_20(target=100):
    from functools import reduce
    return reduce(lambda x, y: int(x)+int(y),[x for x in str(reduce(lambda x, y: x*y, [x for x in range(1, target)]))])

problem_20()
