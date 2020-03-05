def problem_30(target=5):
    return sum([x for x in range(2, 10**(target+1)) if sum([int(y)**target for y in str(x)]) == x])

problem_30()
