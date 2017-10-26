def problem_24(target=1000000):
    from itertools import permutations
    digits = "0123456789"
    return "".join([x for idx, x in enumerate(permutations(digits, len(digits))) if idx == target-1][0])

print(problem_24())
