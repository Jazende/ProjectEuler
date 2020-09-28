from fractions import Fraction

def infinite_function(series, current_position=0):
    if current_position == len(series)-1:
        return series[current_position]
    else:
        return series[current_position] + Fraction(1, infinite_function(series, current_position+1))

def inf_series_for_e(convergent):
    value = 1
    series = [2]
    while True:
        if len(series) > convergent:
            break
        series.append(1)
        series.append(value*2)
        series.append(1)
        value += 1
    return series[:convergent]

def numerator_sum_of_fraction(fraction):
    num = fraction.numerator
    return sum([int(x) for x in str(num)])

if __name__ == '__main__':
    # print(infinite_function([1, 2]), 3/2)
    # print(infinite_function([1, 2, 2]), 7/5)
    # print(infinite_function([1, 2, 2, 2]), 17/12)
    # print(infinite_function([1, 2, 2, 2, 2]), 41/29)

    # print(infinite_function([2, 1, 2, 1, 1, 4, 1, 1, 6, 1]))

    e_series = inf_series_for_e(100)
    conv = infinite_function(e_series)
    sum_ = numerator_sum_of_fraction(conv)
    print(sum_)
    