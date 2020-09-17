from functools import _lru_cache_wrapper, _CacheInfo
import cProfile
from math import gcd

# def problem_073():
#     top = 12000
#     count = 0
#     lower_bound = 0.333333333333334
#     upper_bound = 0.5
#     for denominator in range(4, top+1):
#         lower = int(round(lower_bound * denominator + 0.5, 0))
#         upper = int(round(upper_bound * denominator - 0.5, 0))
#         for numerator in range(lower, upper+1):
#             if not gcd(numerator, denominator) == 1:
#                 continue
#             val = numerator / denominator
#             count += 1
#                 # print(f"{numerator} / {denominator}")
#     print(count)

# cProfile.run('problem_073()')


def farey_function(n, descending=False):
    a, b, c, d = 0, 1, 1, n
    if descending:
        a, c = 1, n-1
    while (c <= n and not descending) or (a > 0 and descending):
        k = int((n + b)/d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        yield (a, b)

gen = farey_function(12000)

count = 0
while True:
    try:
        next(gen)
    except StopIteration:
        count -= 1
        break
    count += 1
print(count)