from math import sqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def get_square(nr):
    return nr*nr

@lru_cache(maxsize=None)
def get_sqrt(nr):
    return sqrt(nr)

def get_path(a, b, c):
##    x = get_square(a) + get_square(b+c)
##    y = get_square(b) + get_square(a+c)
##    z = get_square(c) + get_square(a+b)  
##    return get_sqrt(min(x, y, z))
    return get_sqrt(get_square(a)+get_square(b+c))

count = 0
for a in range(1, 10000):
    for b in range(1, a+1):
        for c in range(1, b+1):
            if get_path(a, b, c).is_integer():
                count+=1
    print(a, count)
    if count > 1000000:
        break
print(count, total)
