import cProfile
from itertools import permutations

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def magnitude(x):
    return int(math.floor(math.log10(x)))

def bounds():
    result = 0
    lower_bounds = [sum([integers[i-1]*10**(y-i) for i in range(1, y+1)]) for y in range(1, 10)]
    upper_bounds = [sum([integers[::-1][i-1]*10**(y-i) for i in range(1, y+1)]) for y in range(1, 10)]
    for i in range(1, 10):
        for j in range(1, 10):
            min_ = len(str(lower_bounds[i-1]*lower_bounds[j-1]))
            max_ = len(str(upper_bounds[i-1]*upper_bounds[j-1]))
            lb = i+j+min_
            ub = i+j+max_
            if lb <= 9 <= ub:
                result = max(i, result)
    return result
    
def euler_32():
    upper_bound = bounds()
    p = permutations(integers)
    results = set()
    while True:
        try:
            perm = next(p)
            for y in range(1, upper_bound+1):
                # 4, 1 of 3, 2 of 2, 3 of 1, 4
                # z = 4 - y + 1
                left_side = sum([perm[i-1]*10**(y-i) for i in range(1, y+1)])
                right_side = sum([perm[y+i-1]*10**(5-y-i) for i in range(1, 6-y)])
                product = left_side*right_side
                list_ = [int(x) for x in str(left_side)+str(right_side)+str(product)]
                if sorted(list_) == integers:
                    results.add(product)
        except StopIteration:
            break
    return sum(results)

print(euler_32())
cProfile.run('euler_32()')
