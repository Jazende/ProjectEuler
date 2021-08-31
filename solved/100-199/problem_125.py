import cProfile
from functools import lru_cache

full_target = 100_000_000
# full_target = 1_000
target = int(full_target ** (1/2))

def is_palindromic(nr):
    return str(nr) == str(nr)[::-1]

@lru_cache(maxsize=None)
def added_square_sum(nr):
    if nr == 0: return 0
    elif nr == 1: return 1
    else:
        return (nr*nr) + added_square_sum(nr-1)

ascending_sums = [added_square_sum(x) for x in range(target*100)]

def calculated():
    found_nrs = set()
    for start in range(1, target+1):
        for end in range(start+1+1, target+1+1):
            nr = ascending_sums[end-1] - ascending_sums[start-1]
            if nr < full_target and is_palindromic(nr):
                found_nrs.add(nr)
    return sum(found_nrs)

print(calculated())