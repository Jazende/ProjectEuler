from math import log10
from math import log
from math import ceil
from math import floor

def problem_63():
    min_ = 2
    def power_of(power):
        # log a (x) = q <-> a ^ q = x
        min_value = 10**(power-1)
        min_range = floor(min_value**(1/power))
        # max_range is altijd 10, 10**x => x+1 digits (1+x*0)
        max_range = 10
        tellen = 0
        for x in range(min_range, 10):
            result = x ** power
            length = len(str(result))
            if length == power:
                tellen += 1
        return tellen

    power = 1
    count = 0
    while True:
        try:
            count += power_of(power)
        except OverflowError:
            break
        power += 1
    return count
