from math import sqrt, floor, ceil
import re

def prob_206():
    target = re.compile('1\d2\d3\d4\d5\d6\d7\d8\d9\d0')
    max_value = 1929394959697989990
    min_value = 1020304050607080900
    min_base = floor(sqrt(min_value)) // 10
    max_base = ceil(sqrt(max_value)) // 10
    print(max_base+1 - min_base)
    for i in range(min_base, max_base+1):
        test = target.match(str((i*10)**2))
        if test:
            print(i*10)
            

prob_206()
